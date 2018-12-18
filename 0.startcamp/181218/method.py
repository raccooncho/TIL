my_list = [4, 7, 9, 1, 3, 6]
max(my_list) # 최댓값
min(my_list) # 최솟값

# 특정 요소의 인덱스?
my_list.index(9)
# list를 뒤집으려면?
my_list.reverse()


dust = 100 # <class : int>
language = 'python' # <class : str>
samsung = ['elec', 'sds', 's1'] # <class : list>

samsung.index('sds') # 1번째 임 (2번째)
samsung.count('s1') # 1개있음

language.capitalize() # 첫자리 대문자로 바꿔줌
language.replace('on', 'off') # (A, B) : A라는 문자열이 포함되어있으면 B로 변경함

samsung.sort() # method 함수들은 원본에 변경을 안주지만 sort 같이 원본을 변경하는 함수도 존재함

samsung.append('bio') # 얘도 원본 포기함. 리스트에 추가하는 것임