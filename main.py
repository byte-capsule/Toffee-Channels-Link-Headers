from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64,requests,urllib,json,os
from urllib.parse import urlparse,urljoin
from datetime import datetime, timedelta
import time
import pytz


def data_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode()
    


def update_time():

    IST = pytz.timezone('Asia/Dhaka')   
    today_date = datetime.now(IST).strftime("%d-%m-%Y") #Current Date
    curr_time = datetime.now(IST).strftime("%H:%M:%S")   #Current time
    #input(type(datetime.now(IST).strftime("%H")))
    if int(datetime.now(IST).strftime("%H"))>=5 and int(datetime.now(IST).strftime("%H"))<18:
        emoji="🌞"
    else:
        emoji="🌙"
    if datetime.now(IST).strftime("%H")<"12":
    	curr_time=curr_time+" AM "+emoji
    else:
    	curr_hour=int(datetime.now(IST).strftime("%H"))-12
    	curr_min=datetime.now(IST).strftime("%M")
    	curr_sec=datetime.now(IST).strftime("%S")
    	curr_time=str(curr_hour)+":"+curr_min+":"+curr_sec
    	curr_time=curr_time+" PM "+emoji
    return curr_time,today_date
    
def load_channel():
	api="https://mapi.toffeelive.com/ugc-app-home-page-content-toffee-v2/1/0/1/200/820"
	headers={
	"Host": "mapi.toffeelive.com",
    "user-agent": "Toffee/5.1.1 (Linux;Android 7.1.2) AndroidXMedia3/1.1.1/64103898/4d2ec9b8c7534adc",
    "client-api-header":"angM1aXCHQLmmSW6cDlpXMD6tLdwnhMoUeaBBFKmd98bX6Vrae5xCMbm4gg0+u33rnxeGQDZNr2GD1tW0cWwKEpWimNlGqXVQGhpiIBz1JFxN+OxXcQqaMPrjwUhCyI5mO1DGyNv18+Z2EpmHtVnLzV9SrGsQWu4oRKjxE8QIMsRs6LrvL6hWGPlOGQke/qb5QxQZNetPzI39jHhX7Zi2XrCMIT4a+gk2Wu1c3wIybwkqknPcTp4Bj1cEF3Q+q1dV05SBhzpEDfoR2BLyQ6dV3LvmY6MNKxbUjby7hMsg35lFl2Df2mZsr7C27309w/qWi8lLXDjB7B1MozIGKn8rw3bXY5YlrPKBKztyiisAjQQi7kc5ISXyGSwRmhciwkciuitsSL0LlqHY7/Qkkh71EtaK3XEgVpLdH8zRCsTwfu1iIVPiDwTycuuBy4XWkcNnd0iLB35yftQpiL8HfpO2jQnrAwzePxszJ7mewVG+M0P/qyTBD52NkPR8uW0AZmDKp5LHTCGf7sqldDzpZvU+gsSdvtsBUcmHzjINGEoyXk=",
    "accept-encoding":"gzip"
	}
	req=requests.get(url=api,headers=headers, verify=False)
	categories=json.loads(data_decrypt(secret_key,req.text))["response"]["categories"]
	
	all_data=[]
	for category in categories:
	    category_name=category["category_name"]
	    
	    for channel in category["channels"]:
	        link=channel["plain_hls_url_for_url_type"]
	        program_name=channel["program_name"]+" VIP"
	        if link=="":
	            program_name=channel["program_name"]
	            
	            link=channel["plain_hls_url"]
	        if link.endswith("u8")==False:
	            link=channel["plain_hls_url"]
	            if link.endswith("u8")==False:
	                link=channel["hlsLinks"][0]["hls_url_mobile"]
	                if link.endswith("u8")==False:
	                    link="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
	            
	        data={
	        "category_name":category_name,
	        "name":program_name,
	        "link":link,
	        #"link":channel["hlsLinks"][0]["hls_url_mobile"],    premium tv not working 
	        "headers":{
	        "Host":urlparse(link).netloc,
	        #"Host":urlparse(channel["hlsLinks"][0]["hls_url_mobile"]).netloc,
	        "cookie":channel.get("sign_cookie")
	        },
	        "logo":channel["channel_logo"]
	        }
	        all_data.append(data)
	return all_data    
 
secret_key=os.environ["TOFFEE_KEY"].encode()
data=load_channel()
with open("toffee_channel_data.json","w") as w:
    json.dump(data,w,indent=2)
    
    
