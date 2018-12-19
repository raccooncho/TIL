# 1. 평균을 구하시오 float
my_score = [79, 84, 66, 93]

ams = sum(my_score)
len(my_score)
my_average = ams / len(my_score)
print("나의 평균 점수는", my_average, "입니다.")

your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}

ays = sum(list(your_score.values()))


your_average = ays / len(your_score)
print("당신의 평균 점수는", your_average, "입니다.")


perfect_score = [100, 100, 100, 100]
sps = sum(perfect_score)
perfect_average = sps / len(perfect_score)
print(perfect_average)