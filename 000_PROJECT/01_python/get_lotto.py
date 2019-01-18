"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"

import requests

URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(URL)

print(response)


