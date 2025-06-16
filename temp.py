import json

from ollama_client import OllamaClient
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from abc import abstractmethod
from dataclasses import dataclass
from typing import List
import re
import sys
import os
import requests
from datetime import datetime
from logging_config_p import logger
from fake_useragent import UserAgent
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

NEWS_JSON_FILE_NAME = "news_results.json"
PROCESSED_NEWS_JSON_FILE_NAME = "news_results_processed.json"
CN_NEWS_FOLDER_NAME = "news"
FINAL_VIDEOS_FOLDER_NAME = "final_videos"
EVENING_TAG = "_E"
EVENING = False
CHINADAILY = 'chinadaily'
CHINADAILY_EN = 'chinadaily_en'
CHINADAILY_HK = 'chinadaily_hk'
ALJ = 'alj'
CFR = 'cfr'
BBC = 'bbc'

AUDIO_FILE_NAME = "summary_audio.mp3"

SUB_COUNT = 15

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809',
}


def generate_audio(text: str, output_file: str = "audio.wav", name='zh-CN-XiaoxiaoNeural',rewrite=False) -> None:
    logger.info(f"{output_file}开始生成音频: {text}")
    rate = 70
    sh = f'edge-tts --voice {name} --text "{text}" --write-media {output_file} --rate="+{rate}%"'
    os.system(sh)

def voice_verify():
    for i in  ['zh-CN-XiaoxiaoNeural','zh-CN-XiaoyiNeural','zh-TW-HsiaoChenNeural','zh-TW-HsiaoYuNeural','zh-CN-liaoning-XiaobeiNeural','zh-CN-shaanxi-XiaoniNeural']:
        generate_audio("你好，这一个清澈见底工的测试", output_file=f"temp/{i}audio.wav", name = i)


def proxy_verify():
    # url = 'https://www.aljazeera.com/'
    url = 'https://www.bbc.com'
    try:
        print(url)
        ua = UserAgent()

        ua_random = ua.random
        headers = {"User-Agent": ua_random,
                   "Accept-Language": "en-US,en;q=0.9", "DNT": "1",
                   "Connection": "keep-alive",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Upgrade-Insecure-Requests": "1"
                   }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(response.text)
    except requests.RequestException as e:
        print(f"fetch_page请求失败: {url} 错误信息： {e}")


if __name__ == '__main__':
    voice_verify()
