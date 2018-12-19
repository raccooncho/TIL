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
print("금주의 당첨번호는", real_numbers, "입니다.", "보너스 번호는", bonus_number, "입니다.")
numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print("나의 번호는", sorted(my_numbers), "입니다.")

set_my_numbers = set(my_numbers)
set_real_numbers = set(real_numbers)
match_numbers = len(set_my_numbers.intersection(set_real_numbers))
print("맞춘 번호는", match_numbers, "개 입니다.")
if match_numbers == 6:
    print("1등")
elif match_numbers == 5:
    if bonus_number in my_numbers:
        print("2등")
    else:
        print("3등")
elif match_numbers == 4:
    print("4등")
elif match_numbers ==3:
    print("3등")
else:
    print("꼴등")


        