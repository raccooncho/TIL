import random
import requests

# my_numbers = pick_lotto()

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers   # 이걸 안하면 함수가 None을 출력함. 없어도 동작할수는 있음.
 


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

# result = am_i_lucky(my_numbers, real_numbers)

def am_i_lucky(pick_num, draw_no):
    real_num = get_lotto(draw_no)
    match_number = len(set(pick_num) & set(real_num['numbers']))
    if match_number == 6:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '1등')
    elif match_number == 5 and real_num['bonus'] in pick_num:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '2등')
    elif match_number == 5:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '3등')
    elif match_number == 4:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '4등')
    elif match_number == 3:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '5등')
    else:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '꼴등')

am_i_lucky(pick_lotto(), 800) # print() 함수가 am_i_lucky()함수 안에 내장되어 있음
WYL = am_i_lucky(pick_lotto(), 10)

def main():
    print(pick_lotto())
    print(get_lotto(837))
    print(" 당신의 번호는", WYL[0], "입니다.\n",  # WYL[0] = pick_num (내가 고른 숫자)
        WYL[1], "회차의 당첨 번호는", WYL[2], "이고,\n", # WYL[1] = draw_no (회차 정보) / WYL[2] = real_num['numbers'] (당첨번호)
        "2등 보너스 번호는", WYL[3], "입니다.\n", # WYL[3] = real_num['bonus'] (보너스 숫자)
        "맞은 갯수는", WYL[4], "개 입니다.\n",  # WYL[4] = match_number (맞은 숫자 갯수)
        "당신은", WYL[5], "입니다.") # WYL[5] = 등수

if __name__ == '__main__':
    main()