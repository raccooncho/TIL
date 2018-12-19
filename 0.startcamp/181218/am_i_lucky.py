import random
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)
response.text # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨

bonus_number = lotto_data['bnusNo']

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(sorted(my_numbers))

for i in my_numbers:
    if sorted(my_numbers) == sorted(real_numbers):
        print('1등')
    else:
        print('꼴등')
        