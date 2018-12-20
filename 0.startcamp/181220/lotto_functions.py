import random
import requests

# my_numbers = pick_lotto()

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers   # 이걸 안하면 함수가 None을 출력함. 없어도 동작할수는 있음.
 
print(pick_lotto())

# real_numbers = get_lotto()

def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)
    response = requests.get(url)
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

real_numbers = get_lotto(3) # 3에 들어가는 부분은 arg (arguments)로 부름
print(real_numbers)

# result = am_i_lucky(my_numbers, real_numbers)

def am_i_lucky(pick_num, draw_no):
    real_num = get_lotto(draw_no)
    match_number = len(set(pick_num) & set(real_num['numbers']))
    print("당신의 번호는", pick_num, "입니다.")
    print(draw_no, "회차의 당첨 번호는", real_num['numbers'], "이고,")
    print("2등 보너스 번호는", real_num['bonus'], "입니다")
    print("맞은 갯수는", match_number, "개 입니다.")
    if match_number == 6:
        print("당신은 1등입니다")
    elif match_number == 5 and bonus in pick_num:
        print("당신은 2등입니다")
    elif match_number == 5:
        print("당신은 3등입니다")
    elif match_number == 4:
        print("당신은 4등입니다")
    elif match_number == 3:
        print("당신은 5등입니다")
    else:
        print("당신은 꼴등입니다")

am_i_lucky(pick_lotto(), 24) # print() 함수가 am_i_lucky()함수 안에 내장되어 있음

