
<h1 alig
<h1 align="center">
  <br>
  <a href="https://play.google.com/store/apps/details?id=com.banglalink.toffee"><img src="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/toffee_logo.jpeg" alt="🔥 Toffee 🔥" width="200"></a>
  <br>
  🔥 Toffee 🔥
  <br>
</h1>

<h2 align="center">A Script to trigger the GitHub Actions every day to update the Toffee Channels Link and Cookie </h2>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>



![screenshot](https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/images%20(1).jpeg)

## Key Features

* All The Channel Links and Cookies Are Updated Every 30 Minutes
* No Need to Decrypt The API Data Of Toffee
* The script Can Decrypt The Encrypted Data of Toffee API
* In JSON Format
* You Can Easily Use This on a Website or in an App



## How To Use

* You Can Get The Data Via Get Request




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
    


print(link)
print(headers)
#Request Toffee Main Api With Headers
request_server=requests.get(link,headers=headers)
#Get the Live m3u3 Link
print(request_server.text)


```

> **Note**
> I'm using Python 3.You can use other Languages.

Optput
> ✓ channel link :https://bldcmprod-cdn.toffeelive.com/cdn/live/comedy_central_hd/playlist.m3u8
✓ channel Headers : {'Host': 'bldcmprod-cdn.toffeelive.com', 'cookie': 'Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1698080619:KeyName=prod_linear:Signature=RY1grOoqltoX1yPO4WMzHCQk2xIp1zGvi03K2bdefb-_QErIqzbuBwytBNV5HiSHSsDslAS2gJsuRFT_MnNJCQ'}
✓ Response From Toffee Server : #EXTM3U
#EXT-X-VERSION:3

>#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1024000,RESOLUTION=1280x720
../slang/comedy_central_hd_576/comedy_central_hd_576.m3u8?bitrate=1000000&channel=comedy_central_hd_576&gp_id=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=768000,RESOLUTION=854x480
../slang/comedy_central_hd_320/comedy_central_hd_320.m3u8?bitrate=768000&channel=comedy_central_hd_320&gp_id=

> #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=512000,RESOLUTION=640x360
../slang/comedy_central_hd_160/comedy_central_hd_160.m3u8?bitrate=512000&channel=comedy_central_hd_160&gp_id=


[Program finished]

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

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)
n="center">
  <br>
  <a href="https://play.google.com/store/apps/details?id=com.banglalink.toffee"><img src="https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/toffee_logo.jpeg" alt="🔥 Toffee 🔥" width="200"></a>
  <br>
  🔥 Toffee 🔥
  <br>
</h1>

<h2 align="center">A Script to trigger the GitHub Actions every day to update the Toffee Channels Link and Cookie </h2>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>



![screenshot](https://github.com/Jeshan-akand/Toffee-Channels-Link-Headers/blob/main/images%20(1).jpeg)

## Key Features

* All The Channel Links and Cookies Are Updated Every 30 Minutes
* No Need to Decrypt The API Data Of Toffee
* The script Can Decrypt The Encrypted Data of Toffee API
* In JSON Format
* You Can Easily Use This on a Website or in an App



## How To Use

* You Can Get The Data Via Get Request




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
> ✓ channel Headers : {'Host': 'bldcmprod-cdn.toffeelive.com', 'cookie': 'Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1698080619:KeyName=prod_linear:Signature=RY1grOoqltoX1yPO4WMzHCQk2xIp1zGvi03K2bdefb-_QErIqzbuBwytBNV5HiSHSsDslAS2gJsuRFT_MnNJCQ'}
> ✓ Response From Toffee Server : #EXTM3U
#EXT-X-VERSION:3

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1024000,RESOLUTION=1280x720
../slang/comedy_central_hd_576/comedy_central_hd_576.m3u8?bitrate=1000000&channel=comedy_central_hd_576&gp_id=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=768000,RESOLUTION=854x480
../slang/comedy_central_hd_320/comedy_central_hd_320.m3u8?bitrate=768000&channel=comedy_central_hd_320&gp_id=

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=512000,RESOLUTION=640x360
../slang/comedy_central_hd_160/comedy_central_hd_160.m3u8?bitrate=512000&channel=comedy_central_hd_160&gp_id=


[Program finished]

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

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)
