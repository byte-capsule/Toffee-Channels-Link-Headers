




<h1 align="center">
  <br>
  <a href="https://play.google.com/store/apps/details?id=com.banglalink.toffee"><img src="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/toffee_logo.jpeg" alt="🔥 Toffee 🔥" width="200"></a>
  <br>
  🔥 Toffee 🔥
  <br>
</h1>

<h2 align="center">A Script to trigger the GitHub Actions every day to update the Toffee Channels Link and Cookie </h2>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Made_With-Python%2B-blue"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://img.shields.io/badge/Made%20in-Bangladesh_🇧🇩-green?colorA=%23ff0000&colorB=%23017e40&style=flat-square"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/App-Toffee.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<h1 align="center">
 <a href="https://play.google.com/store/apps/details?id=com.banglalink.toffee"><img src="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/images%20(1).jpeg"></a>
</h1>

## Introdicton 
* [Toffee](https://play.google.com/store/apps/details?id=com.banglalink.toffee) Live is the number 1 entertainment app in Bangladesh, boasting over 10 million downloads on the Google Play Store.
* Toffee uses the AES Encryption Algorithm to secure HTTPS communication with the API Server. If you're looking to scrape channel links from the Toffee API, you'll need to decrypt it using a secret key.
* This script decrypts the Encrypted data and captures all the channel links and headers from the Toffee API, making it easy for you to use on your website or App.

## Key Features

* All The Channel Links and Cookies Are Updated Every 30 Minutes
* Premium Channels Are Also Working
* Contains Link With Headers (Host, Cookie)
* No Need to Decrypt The API Data Of Toffee
* The script Can Decrypt The Encrypted Data of Toffee API
* In JSON Format
* You Can Easily Use This on a Website or in an App for Restreaming TV Channels 



## How To Use
* 👉 **[Auto Updated Channels Json File](https://raw.githubusercontent.com/Jeshan-akand/Toffee-Channels-Link-Headers/main/toffee_channel_data.json)**
* Use Get Request




```python
import requests
#Get updated the Link and Headers 
link="https://raw.githubusercontent.com/Jeshan-akand/Toffee-Channels-Link-Headers/main/toffee_channel_data.json"
request=requests.get(link).json()

name=request["name"]
owner=request["owner"]
channels_amount=request["channels_amount"]
channels_data=request["channels"]
for channel in channels_data:
    link=channel["link"]
    headers=channel["headers"]
    


print("✓ channel link :"+link)
print("✓ channel Headers :",headers)
#Request Toffee Main Api With Headers
request_server=requests.get(link,headers=headers)
#Get the Live m3u3 Link
print("✓ Response From Toffee Server : "+request_server.text)


```

> **Note**
> I'm using Python 3.You can use other Languages.

## Optput
> ✓ channel link :https://bldcmprod-cdn.toffeelive.com/cdn/live/comedy_central_hd/playlist.m3u8
✓ channel Headers : {'Host': 'bldcmprod-cdn.toffeelive.com', 'cookie': 'Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1698080619:KeyName=prod_linear:Signature=RY1grOoqltoX1yPO4WMzHCQk2xIp1zGvi03K2bdefb-_QErIqzbuBwytBNV5HiSHSsDslAS2gJsuRFT_MnNJCQ'}

> ✓ Response From Toffee Server :
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1024000,RESOLUTION=1280x720
../slang/comedy_central_hd_576/comedy_central_hd_576.m3u8?bitrate=1000000&channel=comedy_central_hd_576&gp_id=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=768000,RESOLUTION=854x480
../slang/comedy_central_hd_320/comedy_central_hd_320.m3u8?bitrate=768000&channel=comedy_central_hd_320&gp_id=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=512000,RESOLUTION=640x360
../slang/comedy_central_hd_160/comedy_central_hd_160.m3u8?bitrate=512000&channel=comedy_central_hd_160&gp_id=


> [Program finished]
<h1 align="center">
 <a href="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/toffee_channel_data.json"><img src="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/json.jpg"></a>
</h1>

## Credits

This software uses the following packages:

- [Pydorid 3](http://electron.atom.io/)
- [Termux](https://nodejs.org/)






## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>

## License

MIT

---


## Find Me on 

- [![Github](https://img.shields.io/badge/Github-Byte_Capsule-purple?style=for-the-badge&logo=github)](https://github.com/byte-capsule)

- [![Gmail](https://img.shields.io/badge/Gmail-Byte_Capsule-green?style=for-the-badge&logo=gmail)](mailto:jeshanakand2017@gmail.com)

- [![Facebook](https://img.shields.io/badge/Facebook-Jeshan_Akand-blue?style=for-the-badge&logo=facebook)](https://facebook.com/js929js)

- [![Messenger](https://img.shields.io/badge/Messenger-Jeshan_Akand-orange?style=for-the-badge&logo=messenger)](https://m.me/js929js)

- [![Telegram](https://img.shields.io/badge/Telegram-Byte_Capsule-indigo?style=for-the-badge&logo=telegram)](https://t.me/J_9X_H_9X_N)




















