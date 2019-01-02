def avg(numbers):
    return sum(numbers) / len(numbers)

def cube(x):
    return x * x * x



def main():
    my_score = [79, 84, 66, 93]
    print(avg(my_score))
    print(cube(3))
    print(3 ** 3)

if __name__ == '__main__':
    main()