# -- coding: utf-8 --
import os
import sys
from curl_cffi import requests

NS_RANDOM = os.environ.get("NS_RANDOM","false")
NS_COOKIE = os.environ.get("NS_COOKIE","")
COOKIE = os.environ.get("COOKIE", "")
COOKIE_ENV = NS_COOKIE or COOKIE

pushplus_token = os.environ.get("PUSHPLUS_TOKEN")
telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN","")
chat_id = os.environ.get("CHAT_ID","")
telegram_api_url = os.environ.get("TELEGRAM_API_URL","https://api.telegram.org") # 代理api,可以使用自己的反代
def telegram_Bot(token,chat_id,message):
    url = f'{telegram_api_url}/bot{7481906122:AAG_D9bBJYvCWeqsTmPqDVmAbQWTkYVjGu4}/sendMessage
    data = {
        'chat_id': chat_id,
        'text': message
    }
    r = requests.post(url, json=data)
    response_data = r.json()
    msg = response_data['ok']
    print(f"telegram推送结果：{msg}\n")
def pushplus_ts(token, rw, msg):
    url = 'https://www.pushplus.plus/send/'
    data = {
        "token": token,
        "title": rw,
        "content": msg
    }
    r = requests.post(url, json=data)
    msg = r.json().get('msg', None)
    print(f'pushplus推送结果：{msg}\n')

def load_send():
    global send
    global hadsend
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
            hadsend=True
        except:
            print("加载notify.py的通知服务失败，请检查~")
            hadsend=False
    else:
        print("加载通知服务失败,缺少notify.py文件")
        hadsend=False
load_send()

if COOKIE_ENV:
    url = f"https://www.nodeseek.com/api/attendance?random={session=e8c07b8fc9191ea285a6153afe73f9a4; smac=1726455181-YDSOl7jH3fnyDkz6CFD8xricdSWTLjaJ5LfBTms9KyM; sortBy=postTime; colorscheme=light; hmti_=1727121494-ExgAYTsBy5xB-9XKu47__IakyRmJwNWXy2y8bOt_omEg; cf_clearance=m7A_t_kgRau6VcFp2wX4zbDVHg_5kt3pLwXf9s_iUTM-1727134003-1.2.1.1-A8U5tpQYp7rq29bpnFT3etZODN_1pigK_i5H_fjj3QBLrrQ49u4DimmEMU79Rf__MgKBvHEhoUMOR_FIL2r5Ma7tI0ru8a5tiKh2l.7ZBlx1eMPzBNXYCRbIg0qq.V1utfAa4rmrDx_YZQAhfQDGzTvG0YsxPYsCO_y5EUh1TrfWOzKubtp_qCBCI0qYfTLdqamdvbVpcJItyQeIWTRl_ga8Sf7QaDdnOR_8MLnAODQ7h7jMs7UT88.Nfcg766gr._cuCkv9e366YxnLundfEyUp35ibV0uyeRTWBpC5TAH7e6QWPB5RBO7iEKYUmHltJJ9p_8sysu0IwedboKxBly7UG50MMFydbJxELWxejaxuEm3SeM.I1iNPyqc6azpJ6TmbPy9hVEZd7mAJTD80Yg}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        'sec-ch-ua': "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'origin': "https://www.nodeseek.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.nodeseek.com/board",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        'Cookie': COOKIE_ENV
    }

    try:
        response = requests.post(url, headers=headers,impersonate="chrome110")
        response_data = response.json()
        print(response_data)
        print(COOKIE_ENV)
        message = response_data.get('message')
        success = response_data.get('success')
        send("nodeseek签到", message)
        if success == "true":
            print(message)
            if telegram_bot_token and chat_id:
                telegram_Bot(telegram_bot_token, chat_id, message)
        else:
            print(message)
            if telegram_bot_token and chat_id:
                telegram_Bot(telegram_bot_token, chat_id, message)
            if pushplus_token:
                pushplus_ts(pushplus_token, "nodeseek签到", message)
    except Exception as e:
        print("发生异常:", e)
        print("实际响应内容:", response.text)
else:
    print("请先设置Cookie")
