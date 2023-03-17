

class test003():
    pass


if __name__ == '__main__':

    try:
        # b='001'
        a =b
        print(a)
    except SyntaxError :
        print("我是谁")
    except SystemExit:
        print("你是谁")
    except :
        print("你去哪里")
    else:
        print("我来自哪里")
    finally:
        print("老子数到山")
        # 如果什么都不做，就直接用pass
        pass
    print("+++我去哪里")
