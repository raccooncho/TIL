import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)
response.text # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.appent(value)

print(sorted(real_numbers))
bonus_number = lotto_data['bnusNo']






# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6']
# ]

# print(real_numbers)