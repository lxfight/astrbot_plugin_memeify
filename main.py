from astrbot.api.provider import LLMResponse
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.all import *
from astrbot.api.message_components import *
from astrbot.core.log import LogManager

import re
import os
import random

from .get_meme_image import get_meme_images

@register("Memeify", "lxfight", "一个AstrBot的插件，用于LLM回复表情包的实现", "1.0.0", "https://github.com/lxfight/astrbot_plugin_memeify")
class Memeify(Star):
    def __init__(self, context: Context, config: dict):
        super().__init__(context)
        self.config = config
        
        # 设置日志
        self.logger = LogManager.GetLogger(log_name="memeify")
        
        self.meme_text = []
        self.max_page = {}

    def _load_file(self, file_path):
        """
            加载指定路径的文件内容，返回JSON数据
        """
        if not os.path.exists(file_path):
            self.logger.error(f"文件 {file_path} 不存在，无法加载。")
            return None
        
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            self.logger.error(f"文件 {file_path} 内容无法解析为JSON。")
            return None
            

    @filter.on_llm_response(priority=10) 
    async def on_llm_resp(self, event: AstrMessageEvent, response: LLMResponse):
        """
            处理 LLM 响应，提取出表情词
        """
        if not response or not response.completion_text:
            return
        
        content = response.completion_text
        
        # 定义表情正则模式
        patterns = [
            r'\[([^\]]+)\]',  # [开心]
        ]
        
        # 提取所有符合正则模式的表情内容
        self.meme_text = re.findall(patterns[0], content) 
        self.logger.debug(f"提取到的表情词：{self.meme_text}")


        # 在原消息中去除表情并用" "替换
        response.completion_text = re.sub(patterns[0], '', content)
        self.logger.debug(f"去除后的消息：{response.completion_text}")




    @filter.on_decorating_result()
    async def on_decorating_result(self, event: AstrMessageEvent):
        """
            在发送前构建消息
        """
        # 没有表情
        if not self.meme_text:
            return 

        result = event.get_result()
        if not result:
            return

        chain = result.chain
        for item in self.meme_text:
            if item in self.max_page:
                page = random.randint(1,self.max_page[item])
            else:
                page = 1
            image_url = self._get_image(words=item, page=page)
            if image_url:
                chain.append(Image.fromURL(image_url))

        self.logger.debug(chain) # 打印消息链

    def _get_image(self, words, page = 1):
        """
            获取图片
        """
        result = get_meme_images(
                apihz_id = self.config.apihz_id,
                apihz_key = self.config.apihz_key,
                words = words,
                limit = self.config.limit,
                page = page
            )
        if result['code'] == 200:
            if words not in self.max_page and 'maxpage' in result:
                self.max_page[words] = result['maxpage']
            image_url = random.choice(result['res'])
            self.logger.info(f"图片：{image_url}")
            return image_url
        else:
            self.logger.error(result)
            return None
