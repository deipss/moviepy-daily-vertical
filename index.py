import os
import json
import gradio as gr
from datetime import datetime
from logging_config_p import logger
from video_generator_portrait import combine_videos, build_new_articles_uploaded_path, ALJ_UP

# 保存目录
VIDEO_DIR = "news_p"
os.makedirs(VIDEO_DIR, exist_ok=True)
ROW = 8


def generate_audio(text: str, output_file: str = "audio.wav", rewrite=False) -> None:
    logger.info(f"{output_file}开始生成音频: {text}")
    rate = 70
    sh = f'edge-tts --voice zh-CN-YunjianNeural --text "{text}" --write-media {output_file} --rate="+{rate}%"'
    os.system(sh)


def save_videos(*args):
    try:
        video_info = []
        today = datetime.now().strftime('%Y%m%d')
        times = int(args[-2])
        row_title = f'{today}竖屏_{times} '
        contents = []
        titles = []

        for i in range(ROW):
            video_file = args[i * 3]
            if not video_file:
                logger.warning(f"{i}视频是空的")
                continue
            title_i = args[i * 3 + 1].replace('\n', '').replace(' ', '')
            description_i = args[i * 3 + 2].replace('\n', '').replace(' ', '')
            contents.append(str(i) + description_i)
            titles.append(title_i)
            if not (video_file and title_i and description_i):
                return f" 第{i + 1}组信息不完整，请检查。"

            # 保存视频文件
            filename = f"{times}_{title_i}.mp4"
            uploaded_video_path = os.path.join(VIDEO_DIR, today, ALJ_UP, filename)
            os.makedirs(os.path.dirname(uploaded_video_path), exist_ok=True)
            with open(video_file.name, "rb") as src_file:
                with open(uploaded_video_path, "wb") as out_file:
                    out_file.write(src_file.read())
            logger.info(f'video has saved in {uploaded_video_path}')
            mp3_path = f"{times}_{title_i}.mp3"
            mp3_path = os.path.join(VIDEO_DIR, today, ALJ_UP, mp3_path)

            generate_audio(description_i, mp3_path)
            logger.info(f'mp3 has saved in {mp3_path}')
            video_info.append({
                "video": uploaded_video_path,
                "audio": mp3_path,
                "title": title_i,
                "summary": description_i,
                "source": ALJ_UP,
                "show": True
            })
            # 保存为 JSON
        saved_json_file = build_new_articles_uploaded_path(today=today, times_tag=times)
        logger.info(f"video_info has saved in {saved_json_file}")
        with open(saved_json_file, "w", encoding="utf-8") as f:
            json.dump(video_info, f, ensure_ascii=False, indent=2)
        combine_videos(today, times_tag=times)

        row_title += ' '.join(titles)
        return_txt = [row_title]
        return_txt.extend(contents)
        show_txt = '\n'.join(return_txt)
        logger.info(f"return_txt = {show_txt}")
        return show_txt
    except Exception as e:
        logger.error(f"上传失败: {e}", exc_info=True)
        return f"上传失败: {str(e)}"


if __name__ == '__main__':

    with gr.Blocks() as app:
        with gr.Row():
            # 左侧：上传区
            with gr.Column(scale=4):
                inputs = []
                for i in range(ROW // 2):  # Adjust loop to handle two columns
                    with gr.Row():  # Create two columns for each row
                        for j in range(2):  # For two videos per row
                            with gr.Column():
                                gr.Markdown(f"### 视频 {i * 2 + j + 1}")
                                video = gr.File(label="上传视频", file_types=["video"], file_count="single", scale=1,
                                                height=80)
                                title = gr.Textbox(label="视频名称")
                                description = gr.Textbox(label="视频描述", lines=2)
                                inputs.extend([video, title, description])

            # 右侧：输出结果区
            with gr.Column(scale=2):
                title_main = gr.Textbox(label="生成视频名称")
                times = gr.Number(label="生成视频序号[只能数字]", precision=0)
                inputs.append(times)
                inputs.append(title_main)
                submit_btn = gr.Button("上传所有视频")
                result_output = gr.Textbox(label="上传结果", lines=10, interactive=False)

        submit_btn.click(fn=save_videos, inputs=inputs, outputs=result_output)
    app.launch(server_port=7860)
