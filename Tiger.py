#ex) 79 import
def f1():
    print(1)

def f2():
    print(__name__)
    print(123)



if __name__ == '__main__':
    print('f1')
    print(1234567)





def main():
    print(1)

if __name__ == '__main__':     # 엔트리 포인트, 진입점
    def f3():
        print(2)
    main()

f3()