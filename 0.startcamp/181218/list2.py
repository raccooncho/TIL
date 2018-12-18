team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

type(team[2:4]) # slicing 하면 무조건 list로 추출됨

new_member = ['js', 10]
team = team + new_member # list끼리 합치기 가능함
team += new_member # 중복되는 문구는 +=으로 대체 가능
print(team)

del(team[-2:]) # 삭제 가능
print(len(team))