# 1. 技术方案

使用gradio作为用户接口的框架，让用户上传若干视频，将新闻的文字，生成音频，最终组合为一个音频

# 2. 新闻来源

- [x] 中国日报（chinadaily）
- [x] 英国广播公司（BBC）
- [x] 中东半岛新闻 https://www.aljazeera.com/

# 3. 使用

在ubuntu 22.04 中，使用conda创建一个python3.11的环境，安装依赖包，然后运行crawl_news.py和vedio_generator.py。

> 要先使用python crawl_news.py，下载好的数据，再调用video_generator.py生成视频。

```shell
nohup python index.py 2>&1 & 
```

# 4. 效果

生成的视频截图
![img_1.png](assets/img_1.png)

操作界面的截图
![img.png](assets/img.png)

# 5. 附件

爬取的数据样例：

```json
[
  {
    "video": "news_p/20250616/alj_up/2_以色列空袭伊朗马什哈德机场.mp4",
    "audio": "news_p/20250616/alj_up/2_以色列空袭伊朗马什哈德机场.mp3",
    "title": "以色列空袭伊朗马什哈德机场",
    "summary": "6 月 15 日傍晚，以色列国防军称，以空军在伊朗马什哈德机场击落一架空中加油机，该机场距以约 2300 公里 。目前伊朗官方尚未回应，地区局势或再升级。",
    "source": "alj_up",
    "show": true
  },
  {
    "video": "news_p/20250616/alj_up/2_特朗普生日盛大军事游行.mp4",
    "audio": "news_p/20250616/alj_up/2_特朗普生日盛大军事游行.mp3",
    "title": "特朗普生日盛大军事游行",
    "summary": "特朗普生日之际，迎来期盼多年的盛大军事游行。坦克与部队亮相华盛顿特区，此次游行恰逢陆军成立 250 周年纪念，场面壮观。",
    "source": "alj_up",
    "show": true
  },
  {
    "video": "news_p/20250616/alj_up/2_以色列总理内塔尼亚胡视察伊朗遭袭地点.mp4",
    "audio": "news_p/20250616/alj_up/2_以色列总理内塔尼亚胡视察伊朗遭袭地点.mp3",
    "title": "以色列总理内塔尼亚胡视察伊朗遭袭地点",
    "summary": "此次视察举动引发外界对地区局势走向及以伊关系动态的密切关注。在此期间，因部分人员仍被困于废墟之下，救援行动正在紧张开展。救援力量全力投入，争分夺秒拯救生命，局势备受关注。",
    "source": "alj_up",
    "show": true
  }
]
```