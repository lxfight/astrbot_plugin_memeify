import requests

def get_meme_images(apihz_id, apihz_key, words, limit=1, page=1):
    # 构建请求参数字典
    params = {
        'id': apihz_id,
        'key': apihz_key,
        'type': 2,
        'words': words,
        'page': page,
        'limit': limit
    }
    
    # URL 编码处理（将关键词words进行URL编码）
    if words:
        params['words'] = requests.utils.quote(words)
    
    # 接口地址
    url = 'https://cn.apihz.cn/api/img/apihzbqbbaidu.php'
    
    try:
        # 发送 GET 请求
        response = requests.get(url, params=params)
        
        # 检查是否请求成功
        if response.status_code == 200:
            # 返回 JSON 格式的响应
            return response.json()
        else:
            return {'error': 'Request failed', 'status_code': response.status_code}
    except Exception as e:
        return {'error': str(e)}
