import random
import requests

# my_numbers = pick_lotto()

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers   # 이걸 안하면 함수가 None을 출력함. 없어도 동작할수는 있음.


# real_numbers = get_lotto()

def get_lotto(num):
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='+str(num)
    response = requests.get(url, verify = False)
    lotto_data = response.json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    final_dict = { 
        "numbers": numbers,
         'bonus': bonus_number
         }
    return final_dict
print(get_lotto(836))
# result = am_i_lucky(my_numbers, real_numbers)

def am_i_lucky(a, b):
    match_number = len(set(a) & set(b['numbers']))
    if match_number == 6:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 1등입니다")
    elif match_number == 5 and bonus in a:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 2등입니다")
    elif match_number == 5:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 3등입니다")
    elif match_number == 4:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 4등입니다")
    elif match_number == 3:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 5등입니다")
    else:
        print("당신의 번호는", a, "입니다.", "선택하신 회차의 당첨 번호는", b['numbers'], "+", b['bonus'], "입니다", "맞은 갯수는", match_number, "개 입니다. 당신은 꼴등입니다")

print(am_i_lucky(pick_lotto(), get_lotto(836)))
# url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

# response = requests.get(url, verify = False)
# response.text # 이건 class가 str임
# response.json() # 이게 dict임 이걸 data라고 부름
# lotto_data = response.json()

# real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨

# bonus_number = lotto_data['bnusNo']
# print("금주의 당첨번호는", real_numbers, "입니다.", "보너스 번호는", bonus_number, "입니다.")


# set_my_numbers = set(my_numbers)
# set_real_numbers = set(real_numbers)
# match_numbers = len(set_my_numbers.intersection(set_real_numbers))
# print("맞춘 번호는", match_numbers, "개 입니다.")
# if match_numbers == 6:
#     print("1등")
# elif match_numbers == 5:
#     if bonus_number in my_numbers:
#         print("2등")
#     else:
#         print("3등")
# elif match_numbers == 4:
#     print("4등")
# elif match_numbers ==3:
#     print("5등")
# else:
#     print("꼴등")

# # count = 0
# # while match_numbers:
# #     if match_numbers < 6:
# #         count += 1
# #     else:
# #         print("당첨입니다. 산 복권은", count, "장 입니다.")


