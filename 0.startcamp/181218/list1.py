numbers = [1, 2, 3]   # 변수 이름은 뜻을 담아서 짓자!
family = ['mom', 1.64, 'dad', 1.75, 'sister', 1.78]
mcu = [
    ['Ironman', 'Captain america', 'Dr.strange', 'Hulk', 'Torr'], 
    ['Xmen', 'Deadpool'], 
    ['Spiderman']
    ]
print(mcu[0][2])  # n차원 배열!

lotto_numbers = list(range(1, 46)) # 마지막 숫자는 안나옴 (1~45까지 출력됨) # range 클래스가 list 클래스로 변경됨

int('123') # str인 '123'을 int인 123으로 변경해 줌 # True = 1, False = 0

lotto_numbers[2:5] # [start:end] => start 는 포함, end 는 포함하지 않음!
