import time, random, configparser
import requests

s = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044429 Mobile Safari/537.36 MMWEBID/4665 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools",
    "Referer":"http://weixin.sinatj.com/app/index.php?i=4&c=entry&id=207&rid=117&do=view&m=tyzm_diamondvote&from=singlemessage",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,en-US;q=0.9",
    "X-Requested-With": "XMLHttpRequest"
}

conf = configparser.ConfigParser()
conf.read("voter.ini")

vote_interval_min = conf.getint("timer","vote_interval_min")
vote_interval_max = conf.getint("timer","vote_interval_max")
batch_interval_min = conf.getint("timer","batch_interval_min")
batch_interval_max = conf.getint("timer","batch_interval_max")

def vote_once():
    r = s.post("http://weixin.sinatj.com/app/index.php?i=4&c=entry&rid=117&id=207&do=vote&m=tyzm_diamondvote",
           data={
               "latitude":"0",
               "longitude":"0",
               "verify":"0"
           },
           headers=headers
           )
    assert r.json().get("status") == "1"

def vote_batch():
    for cnt in range(5):
        vote_once()
        print("第{}次投票完成".format(cnt))
        time.sleep(random.randrange(vote_interval_min,vote_interval_max))


if __name__ == "__main__":
    print('''
    开始刷票, 如果你想改刷票频率, 用笔记本打开vote.ini, 里面4个能改的数分别是:
    最小投票间隔({})
    最大投票间隔({})
    每组投票最小间隔({})
    每组投票最大间隔({})
    PS:改完关了重新跑本程序.
    '''.format(vote_interval_min, vote_interval_max, batch_interval_min, batch_interval_max))
    cnt = 1
    while True:
        vote_batch()
        print("第{}组投票完成".format(cnt))
        cnt=cnt+1
        time.sleep(random.randrange(batch_interval_min,batch_interval_max))