# 1. 技术方案

使用gradio作为用户接口的框架，让用户上传若干视频，将新闻的文字，生成音频，最终组合为一个音频

# 2. 新闻来源

- [x] 中国日报（chinadaily）
- [x] 英国广播公司（BBC）

# 3. 使用

在ubuntu 22.04 中，使用conda创建一个python3.11的环境，安装依赖包，然后运行crawl_news.py和vedio_generator.py。

> 要先使用python crawl_news.py，下载好的数据，再调用video_generator.py生成视频。

```shell
nohup python index.py 2>&1 & 
```

# 4. 效果

以下生成的视频截图
![img.png](assets/img.png)

# 5. 附件

爬取的数据样例：

```json

```