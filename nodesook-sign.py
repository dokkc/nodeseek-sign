
import requests

def send_post_request_with_cookie(url):
    """
    发送带有Cookie的POST请求

    Args:
        url (str): 请求URL
        data (dict): 请求数据
        cookies (dict): Cookie字典

    Returns:
        requests.Response: 请求响应对象

        cookie 修改为自己的
    """
    headers = {
        "Cookie": "111",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.nodeseek.com/board",
    }

    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    # 使用示例
    url = "https://www.nodeseek.com/api/attendance?random=true"
    response = send_post_request_with_cookie(url)
    response_json = response.json()
    if "message" in response_json:
        print(response_json["message"])
