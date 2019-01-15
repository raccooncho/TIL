import turtle as t
import random



class MagicBrush:
    def draw_sqare(self, n):
        t.color('yellow')
        for i in range(4):
            t.forward(n)
            t.right(90)
    def draw_triangle(self, n):
        t.color('blue')
        for i in range(3):
            t.forward(n)
            t.right(120)
    def draw_round(self, n):
        t.color('red')
        for i in range(36):
            t.forward(n/2)
            t.right(10)

    def inf_round(self, n):
        if n == 1:
            self.draw_round(1)
        else:
            self.draw_round(n)
            t.right(72)
            self.inf_round(n-1)
    
    def star(self, n):
        if n > 20:
            a = random.choice(range(20))
            for i in range(5):
                t.forward(a * 3)
                t.right(144)
        else:
            for i in range(5):
                t.forward(3*n)
                t.right(144)
            
    def random_star(self, n):
        t.bgcolor('black')
        t.color('yellow')
        x = random.choice(range(-350, 350))
        y = random.choice(range(-350, 350))
        t.penup()
        t.goto(x, y)
        t.pendown()
        if n == 1:
            self.star(1)
        else:
            self.star(n)
            self.random_star(n-1)
t.shape('turtle')
# t.goto(0, 0)
m1 = MagicBrush()
m1.inf_round(40)
# m1.random_star(30)
# m2 = MagicBrush()
# # m1.draw_sqare(50)   
# # m1.draw_triangle(50)
# m2.draw_round(16)
# t.penup()
# t.goto(-83, -90)
# t.pendown()
# t.forward(185)
# t.penup()
# t.goto(-40, -45)
# t.pendown()
# m2.draw_round(3)
# t.penup()
# t.goto(40, -45)
# t.pendown()
# m2.draw_round(3)
# t.penup()
# t.left(90) 
# t.forward(180)
# t.pendown()
# t.right(90)
# for i in range(36):
#     t.forward(31.4)
#     t.right(10)
# t.right(90)
# t.penup()
# t.forward(180)
# t.right(90)
# t.forward(180)
# t.right(180)
# t.pendown()
# t.forward(360)
# t.right(180)
# t.forward(180)
# t.penup()
# t.right(90)
# t.forward(90)
# t.right(90)
# t.forward(30)
# t.left(90)
# t.pendown()
# for i in range(36):
#     t.forward(3.14)
#     t.right(10)
# t.left(90)
# t.penup()
# t.forward(60)
# t.pendown()
# t.right(90)
# for i in range(36):
#     t.forward(3.14)
#     t.left(10)

t.mainloop()
