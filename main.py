import module
from random import randint


def task3():
    for _ in range(100):
        print(module.task3.div(randint(0, 10), randint(0, 10)))
        try:
            print(module.task3.div(5, 0))
        except ZeroDivisionError as e:
            print(e)


def task4():
    print(module.task4.date_from_text('1-й четверг ноября'))
    print(module.task4.date_from_text('3-я среда мая'))


def task5():
    # you to start with next command
    # python main.py -d 1-й четверг ноября
    out = module.task5.out_parser()
    print(module.task5.date_from_text(out))


def task6():
    # python main.py -p C:\
    out = module.task6.out_parser()
    print(*module.task6.task6(out), sep="\n")


def main():
    # task3()
    # task4()
    # task5()
    task6()


if __name__ == '__main__':
    main()
