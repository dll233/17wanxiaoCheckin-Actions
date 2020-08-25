import time
import datetime
import json
import requests


check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

text = input()
deptId = eval(input())
address = input()
addtext = input()
code = ''
stuNum = input()
print(stuNum,'*'*20)
userName = input()
phoneNum = ''
userId = int(input())
emergency = input()
emergencyPhone = input()
sckey = input()


area = {'address': address, 'text': addtext, 'code': code}

areaStr = json.dumps(area, ensure_ascii=False)

jsons = {"businessType": "epmpics", "method": "submitUpInfo",
        "jsonData": {"deptStr": {"deptid": deptId, "text": text},
                     "areaStr": areaStr,
                     "reportdate": round(time.time()*1000), "customerid": "786", "deptid": deptId, "source": "alipay",
                     "templateid": "pneumonia", "stuNo": stuNum, "username": userName, "phonenum": phoneNum,
                     "userid": userId, "updatainfo": [{"propertyname": "temperature", "value": "36.4"},
                                                        {"propertyname": "symptom", "value": "无症状"},
                                                        {"propertyname": "isConfirmed", "value": "  否"},
                                                        {"propertyname": "isdefinde", "value": "否.未隔离"},
                                                        {"propertyname": "isGoWarningAdress", "value": "否"},
                                                        {"propertyname": "isTouch", "value": "否"},
                                                        {"propertyname": "isTransitArea", "value": "否"},
                                                        {"propertyname": "isTransitProvince", "value": "否"},
                                                        {"propertyname": "isFFHasSymptom", "value": "没有"},
                                                        {"propertyname": "isContactFriendIn14", "value": "没有"},
                                                        {"propertyname": "xinqing", "value": "健康"},
                                                        {"propertyname": "bodyzk", "value": "是"},
                                                        {"propertyname": "cxjh", "value": "否"},
                                                        {"propertyname": "isleaveaddress", "value": "否"},
                                                        {"propertyname": "gtjz0511", "value": "否"},
                                                        {"propertyname": "medicalObservation", "value": "绿色"},
                                                        {"propertyname": "ownPhone", "value": phoneNum},
                                                        {"propertyname": "emergencyContact", "value": emergency},
                                                        {"propertyname": "mergencyPeoplePhone",
                                                         "value": emergencyPhone}], "gpsType": 0}}

response = requests.post(check_url, json=jsons)
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)
print(jsons)


SCKEY = sckey

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%H:%M:%S')}",
    "desp": desp
}
    
# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
        print("Server酱推送服务成功")
else:
        print("Something Wrong")
