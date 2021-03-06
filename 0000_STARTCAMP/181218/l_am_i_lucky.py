import random
import requests

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(sorted(my_numbers))

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url)
response.text # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨

bonus_number = lotto_data['bnusNo']
print("금주의 당첨번호는", real_numbers, "입니다.", "보너스 번호는", bonus_number, "입니다.")


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
    print("5등")
else:
    print("꼴등")

count = 0
check = False
while (True):
    if match_numbers == 0:
        count += 1
    elif match_numbers == 1:
        count += 1
    elif match_numbers == 2:
        count += 1
    elif match_numbers == 3:
        count += 1
    elif match_numbers == 4:
        count += 1
    elif match_numbers == 5:
        count += 1
    else:
        check = True
        print("당첨입니다. 산 복권은", count, "장 입니다.")
        break


# count1 = 0   # 교수님 정답 1
# for my_number in my_numbers:
#     for real_number in real_numbers:
#         if my_number == real_number:
#             count += 1
# print(count1)

# if count1 == 6:
#     print(1)
# elif count1 == 5 and bonus in my_numbers:
#     print(2)
# elif count1 == 5:
#     print(3)


# list = [1, 2, 3]
# set = {1, 2, 3}
# tuple = (1, 2, 3)

# match_count = len(my_numbers % real_numbers)
# print(match_count)

# if match_count == 6:
#     print('1등')
# elif match_count == 5 and bonus in my_numbers:
#     print('2등')


