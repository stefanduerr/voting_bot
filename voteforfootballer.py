import requests
import time
import random

proxies_list = [
    "http://vperbgmt:1cgqi6a20126@185.199.229.156:7492",
    "http://vperbgmt:1cgqi6a20126@185.199.228.220:7300",
    "http://vperbgmt:1cgqi6a20126@185.199.231.45:8382",
    "http://vperbgmt:1cgqi6a20126@188.74.210.207:6286",
    "http://vperbgmt:1cgqi6a20126@188.74.183.10:8279",
    "http://vperbgmt:1cgqi6a20126@188.74.210.21:6100",
    "http://vperbgmt:1cgqi6a20126@45.155.68.129:8133",
    "http://vperbgmt:1cgqi6a20126@154.95.36.199:6893",
    "http://vperbgmt:1cgqi6a20126@45.94.47.66:8110"
]

proxies_list_3 = [
 "http://nuxpfutt:oj6ste7v7hwu@188.74.168.226:5267",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.20:6259",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.90:6329",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.37:5956",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.186:6774",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.90:5131",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.239:6478",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.242:5539",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.89:6328",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.41:5634",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.60:6648",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.7:5600",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.9:5928",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.66:6305",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.68:5987",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.227:6146",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.175:6414",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.101:6340",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.119:6707",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.130:5723",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.116:5157"
]

proxies_list_2 = [
    "http://nuxpfutt:oj6ste7v7hwu@188.74.168.226:5267",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.20:6259",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.90:6329",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.37:5956",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.186:6774",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.90:5131",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.239:6478",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.242:5539",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.89:6328",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.41:5634",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.60:6648",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.7:5600",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.9:5928",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.66:6305",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.68:5987",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.227:6146",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.175:6414",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.101:6340",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.119:6707",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.130:5723",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.116:5157",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.110:6349",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.13:5932",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.91:5132",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.38:6277",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.163:5204",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.146:6734",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.100:6688",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.172:5469",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.183:6771",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.202:6121",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.147:6066",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.122:5163",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.232:6151",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.143:5184",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.140:5181",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.186:5483",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.119:6038",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.222:6810",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.10:6598",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.65:6653",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.87:6006",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.24:6612",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.195:6434",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.202:6441",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.150:5447",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.19:6607",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.199:5240",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.251:6490",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.90:5683",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.205:5798",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.111:5408",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.198:5791",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.198:5239",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.77:6665",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.181:5774",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.205:5246",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.193:5490",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.255:5296",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.118:5711",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.157:6076",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.114:6702",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.46:5639",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.153:6741",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.78:6666",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.5:6593",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.66:6654",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.17:5058",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.220:5261",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.13:6252",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.193:5786",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.228:5821",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.40:6279",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.4:5045",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.101:6020",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.88:5681",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.168:6407",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.249:5290",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.72:5113",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.49:5346",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.74:6313",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.129:6048",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.201:5794",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.142:6730",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.32:5625",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.146:5187",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.73:5114",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.153:6392",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.216:6455",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.194:6782",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.182:5775",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.190:6109",
"http://nuxpfutt:oj6ste7v7hwu@64.137.108.63:5656",
"http://nuxpfutt:oj6ste7v7hwu@64.137.103.251:6839",
"http://nuxpfutt:oj6ste7v7hwu@188.74.168.2:5043",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.31:6270",
"http://nuxpfutt:oj6ste7v7hwu@188.74.169.132:5429",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.85:6004",
"http://nuxpfutt:oj6ste7v7hwu@64.137.88.98:6337",
"http://nuxpfutt:oj6ste7v7hwu@138.128.145.199:6118"
]

url = "https://ticker.ligaportal.at/playerVoting/playerOneUp"
payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voteItem\"\r\n\r\n260318\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"votingId\"\r\n\r\n733\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"g-recaptcha-response\"\r\n\r\n03AL8dmw_7FmtFL7HGmkcxiNlqZlv9GFS5_VI2gugf3tuLINwIwHTW3FL3T58fVv0_0O7PZ-d9WqhMyApIzd-TlFpNzDEc4ZenJY1icxgyX18BQ3jr2ciJoJVUG-9TcOvmWMQVcRcXwzTdOlc0a2-AgzaTFuOdvLMNTcQNtQ7PgKzOy92nB3XZN8YXP_LiqRToRpGqR_8m2UmSuJHDLJFBBP1dqrcKPnkC2roSE7hQobpoNwtc_Ag0H9zWiizKLMpBjWVHAsVG-en3hJQgcl6seGxnaC1ar3BasEn0wxT5LfC-aUewR_pUuxw95BPHuKGxGh-Q4vYdojXu52XpMfHkpBhaDAg0s2GtTzgvesm-ZkyyKeEc6iSqni4iylfYxEQyvwosRf14nRG5shWVDC-bVoyG7CPfFkbh7Aed1Ty05t9-cQ4dzUvDH2MUaChG5Qkg9p_l12aLTUWi6eCUxrM43_R5F-HmN3fB3r6uzCMFN6XJr3fMi4BCTSutvHhUBbPh7T8AItteTjafaHhdy6bX45GzHAH2TJm-xqX5d89VzrC_bG59XJgn5-FV2-CNQQTr97cfDwkUeoc3pJTC47Ey0mFKLXs8yPxfcA\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"playerOneUp\"\r\n\r\nAbstimmen\r\n-----011000010111000001101001--\r\n"
headers = {
    "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}
responseID = 0

for proxy in proxies_list_3:
    responseID += 1
    proxies = {
        "http": proxy,
        "https": proxy
    }

    response = requests.request("POST", url, data=payload, headers=headers, proxies=proxies)
    # print(f'Vote {responseID} cast successfully. Used proxy:')
    # print(proxies)
    # with open(f"{responseID}.html", "w") as f:
    #     f.write(response.text)
    # print(response.headers)

    

    if 'Set-Cookie' in response.headers:
        print('Vote cast sucessfully!')
    else:
        print('You voted already! Try again!')
    
    randInterval = random.randint(1, 6000)
    time.sleep(randInterval/1000)


#curl -x "http://vperbgmt:1cgqi6a20126@185.199.228.220:7300" "https://www.google.com" -I
#https://proxy2.webshare.io/proxy/list?filters=eyJjb3VudHJ5RmlsdGVyIjpbXX0%253D
#https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/storage/#wiki_proxy_lists
#https://www.youtube.com/watch?v=DqtlR0y0suo web scraping tut



# All 8-12 Minutes
timeIntervalRunFrequency = random.randint(48000, 72000)

# Run script 6 times per hour
for x in range(6):
    #script.run()
    pass

# wait up to 60 seconds before starting the script
delayScriptStart = random.randint(0, 60000)

# Proxy Rotation: ~14 Proxies
proxyListIndices = []
while len(proxyListIndices) < 14:
    randomProxy = random.randint(0, 100)
    if randomProxy not in proxyListIndices:
        proxyListIndices.append(randomProxy)

#proxyListIndices = random.sample(range(101), 14)

# Interval between votes: 0-40 sec
timeIntervalBetweenVotes = random.randint(0, 40000)/1000

# Run Script: between 9am-8pm
#https://eu.pythonanywhere.com/user/xjabre/tasks_tab/

# Stop getting same proxies in rotation
