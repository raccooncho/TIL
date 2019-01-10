# 아래에 코드를 작성해주세요.
class Pokemon:
    
    def __init__(self, name, level, element):
        elements = ['elec', 'water', 'fire', 'leef']
        element_attacks = ['10만볼트', '물대포', '화염방사', '잎날가르기']
        self.name = name
        self.level = level
        self.HP = level * 10
        self.vapp = 5
        self.speed = level * 2
        self.element = elements.index(element)
        self.e_attack = element_attacks[self.element]
    def set_HP(self, point):
        self.HP += point
    def check_status(self):
        if self.HP <= 0:
            return False
        else:
            return self.HP
    def body_attack(self, enemy):
        enemy.set_HP(-self.level)
        print(f'{self.name}가 {enemy.name}에게 몸통박치기를 시도하였다.')
        print(f'{self.level}의 데미지를 주었다.')
    def element_attack(self, enemy):
        if self.element == enemy.element + 1:
            if self.vapp > 0:
                print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를 시도하였다.')
                print(f'효과가 부족했다.')
                print(f'{self.level * 1}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 1)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')
        elif self.element == enemy.element - 1:
            if self.vapp > 0:
                print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를 시도하였다.')
                print('효과가 굉장했다.')
                print(f'{self.level * 4}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 4)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')
        else:
            if self.vapp > 0:
                print(f'{self.name}가 {self.enemy.name}에게 {self.e_attack}를 시도하였다.')
                print(f'{self.level * 2}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 2)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')

    
    
    
    
    
a = Pokemon('피카츄', 5, 'elec')
b = Pokemon('꼬북이', 15, 'water')

import random

while a.check_status() and b.check_status():
    if a.speed > b.speed:
        aattack = random.choice([1, 2])
        if aattack == 1:
            a.body_attack(b)
        else:
            a.element_attack(b)
        print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
        if b.check_status() == False:
            break
        battack = random.choice([1, 2])
        if battack == 1:
            b.body_attack(a)
        else:
            b.element_attack(a)
        print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
    elif a.speed == b.speed:
        order = random.choice([1, 2])
        if order == 1:
            aattack = random.choice([1, 2])
            if aattack == 1:
                a.body_attack(b)
            else:
                a.element_attack(b)
            print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
            if b.check_status() == False:
                break
            battack = random.choice([1, 2])
            if battack == 1:
                b.body_attack(a)
            else:
                b.element_attack(a)
            print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
        else:
            battack = random.choice([1, 2])
            if battack == 1:
                b.body_attack(a)
            else:
                b.element_attack(a)
            print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
            if a.check_status() == False:
                break
            aattack = random.choice([1, 2])
            if aattack == 1:
                a.body_attack(b)
            else:
                a.element_attack(b) 
            print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
    else:
        battack = random.choice([1, 2])
        if battack == 1:
            b.body_attack(a)
        else:
            b.element_attack(a)
        print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
        if a.check_status() == False:
            break
        aattack = random.choice([1, 2])
        if aattack == 1:
            a.body_attack(b)
        else:
            a.element_attack(b)
        print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
if a.check_status() == False:
    print(f'{a.name}는 더이상 싸울 힘이 없다.')
    print(f'{b.name}이 전투에서 이기고 {a.level}의 경험치를 획득하였다!!')
else:
    print(f'{b.name}는 더이상 싸울 힘이 없다.')
    print(f'{a.name}이 전투에서 이기고 {b.level}의 경험치를 획득하였다!!')