# IP/MAC/电话/身份证信息查询
在进行安全分析时，经常需要挖掘IP/MAC/电话/身份证/银行卡等背后的信息。基于这个需求，我对IPIP.net的官方查询包进行了丰富。

## 1. 安装说明  
### 1.1 IP数据  
从IPIP.net购买专业版数据，或下载免费版数据，命名为`mydata4vipday2.datx`放置于`datx`目录下。  
### 1.2 MAC地址段分配数据  
MAC数据包含MAC地址段及分配给的公司，这部分数据是公开的。下载以下3个文件放置于`datax`目录下：  
 - https://standards.ieee.org/develop/regauth/oui/oui.csv  
 - https://standards.ieee.org/develop/regauth/oui28/mam.csv  
 - https://standards.ieee.org/develop/regauth/oui36/oui36.csv  
### 1.3 手机归属地数据
从`https://www.qqzeng-ip.com`购买手机号归属地数据phone-qqzeng.csv放置于`datax`目录下。注意要加上csv头：
```
prefix,phone,province,city,isp,post_code,area_code,city_code
```
### 1.4 行政区划代码数据
这部分数据是公开的，但时有更新。在这里我附上，如果有更新按`datax/china_city_code.csv`的格式组织文件即可。
### 1.5 卡bin表
这部分数据也是网上找的，见`https://download.csdn.net/download/qq_37016358/10485816`，不确定真实性和时效性，如果有更新按`datax/card_bin.csv`的格式组织文件即可。
另有一部分分行对应信息表，按`datax/cmb_branch.csv`的格式组织文件。
### 1.6 安装
完成数据下载后，使用`setup.py`安装即可：  
```
python setup.py install
```

## 2. 使用说明
### 2.1 原有IPIP库的使用方式
首先，由于是fork过来的，原有IPIP库的使用方式自然会保留:  
```
import datx

# 查询地级市精度的IP库
c = datx.City("/path/to/mydata4vipday2.datx")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))

# 查询国内区县库
d = datx.District("/path/to/quxian.datx")
print(d.find("123.121.117.72"))

# 查询基站IP库
d = datx.BaseStation("/path/to/station_ip.datx")
print(d.find("223.221.121.0"))
```
### 2.2 拓展后的查询内容
```
from datx import ip2city_info, mac2info, phone2info, idcard2info, city_code2info, card2info, cmb_debit2info
# 查询IP地址
print(ip2city_info('1.12.37.1'))

# 查询MAC地址，至少提供前6位
print(mac2info('8439BE'))
print(mac2info('E8-39-35-0E-97-36'))

# 查询手机号归属地，至少提供前7位
print(phone2info('1387723'))
print(phone2info('13877237171'))

# 查询身份证归属地和年月日，要求提供完整身份证号
print(idcard2info('45020419880704123X'))

# 查询6位行政区划代码（精确到地级市）
print(city_code2info('450204'))

# 查询卡号基本信息
print(card2info('6214830000199527'))

# 查询我行借记卡信息（目前只有开户分行）
print(cmb_debit2info('6214830000199527'))
```