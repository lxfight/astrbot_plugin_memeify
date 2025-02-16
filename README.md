# astrbot_plugin_memeify

一个AstrBot的插件，用于LLM回复表情包的实现。依托[apihz.cn](https://www.apihz.cn)的开放接口，为机器人回复增加表情包匹配能力，提升对话趣味性。

## ✨ 功能特性
- 自动解析文本中的情绪标签
- 动态匹配最符合语境的网络表情包
- 支持文字+图片的多模态回复形式

## 人格设置Prompt
建议在LLM的人格设定prompt中添加：
```markdown
  当表达情绪时，请使用[情绪名称]的标签格式，例如：
  [开心]今天天气真好！ -> 显示开心表情包
  [生气]我不同意这个观点 -> 显示生气表情包
  支持的情绪标签：开心/惊讶/生气/悲伤/期待/疑问
```

##基本配置
前往[apihz.cn](https://www.apihz.cn)注册并获取API密钥

在AstrBot配置文件中添加：
  `apihz_id`和`apihz_key`两个参数即可

## 其他注意事项
- apihz免费用户调用接口限制：10次/分钟
- 默认使用的百度的表情包接口，但你可以换用该网站给出的其他接口，如`搜狗`
  只需要修改`/AstrBot/data/plugins/astrbot_plugin_memeify/get_meme_image.py`文件中的接口地址即可，对于一般用户来说，这项配置无需关注。
- LLM可能生成一些情绪词无法找到对应表情，但这种情况的概率较小。
- 不仅限于情绪词汇，理论上所有词汇都可以作为关键词进行表情包的搜索。

## 🙏 致谢
- 表情包API服务由[apihz.cn](https://www.apihz.cn)独家提供。
- 灵感来源[mccloud_meme_sender](https://github.com/MCYUNIDC/mccloud_meme_sender)。
- AstrBot核心开发团队的技术支持
  
由于作者上网冲浪的时候发现了apihz.cn网站中的表情包API，`astrbot_plugin_meme_manager`项目中使用的是本地的表情，所以`astrbot_plugin_memeify`诞生了。

**Star趋势**：  
[![Star History Chart](https://api.star-history.com/svg?repos=lxfight/astrbot_plugin_memeify)](https://github.com/lxfight/astrbot_plugin_memeify)

如果本项目给您带来欢乐，欢迎点亮⭐️，您的支持是我不断前进的动力！

如果您有任何好的意见和想法，或者发现了bug，请随时提ISSUE，非常欢迎您的反馈和建议。我会认真阅读每一条反馈，并努力改进项目，提供更好的用户体验。

感谢您的支持与关注，期待与您共同进步！
