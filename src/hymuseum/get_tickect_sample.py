import requests

s = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044704 Mobile Safari/537.36 MMWEBID/4665 MicroMessenger/7.0.4.1420(0x2700043A) Process/tools NetType/WIFI Language/zh_CN",
    "Referer":"https://www.hymuseum.org.cn/pw/person/info",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,en-US;q=0.9",
    "X-Requested-With": "com.tencent.mm",
    "Accept": "application/json",
    "Origin": "https://www.hymuseum.org.cn",
    "Connection": "keep-alive",
    "Host": "pw.hymuseum.org.cn"
}

def get_ticket():
    r = s.post("https://www.hymuseum.org.cn/api/ticketorder", verify=False,
               data={
                   "p": "wx",
                   "api_token": "", # set your information
                   "pt_id[0]": "1",
                   "pt_id[1]": "1",
                   "td_tp_id": "33",
                   "toi_username[0]":"",
                   "toi_username[1]":"",
                   "toi_cardtype_id[0]":"1",
                   "toi_cardtype_id[1]":"1",
                   "toi_card_num[0]":"",
                   "toi_card_num[1]":"",
                   "td_tp_ids[0]":"",
                   "td_tp_ids[1]":"",
                   "car_no":""
               },
               headers=headers
               )
    print(r.text)
    return r.json().get("status")

if __name__ == "__main__":
    while True:
        if get_ticket() != 902:
            break