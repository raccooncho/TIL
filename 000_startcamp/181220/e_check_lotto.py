from b_lotto_functions import get_lotto, pick_lotto, am_i_lucky


WYL = am_i_lucky(pick_lotto(), 10)
print(" 당신의 번호는", WYL[0], "입니다.\n",  # WYL[0] = pick_num (내가 고른 숫자)
        WYL[1], "회차의 당첨 번호는", WYL[2], "이고,\n", # WYL[1] = draw_no (회차 정보) / WYL[2] = real_num['numbers'] (당첨번호)
        "2등 보너스 번호는", WYL[3], "입니다.\n", # WYL[3] = real_num['bonus'] (보너스 숫자)
        "맞은 갯수는", WYL[4], "개 입니다.\n",  # WYL[4] = match_number (맞은 숫자 갯수)
        "당신은", WYL[5], "입니다.") # WYL[5] = 등수