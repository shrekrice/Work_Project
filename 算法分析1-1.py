#利用欧几里得算法，将一个给定的真分数化简为最简分数形式。例如，将12/16化简，并生成运行结果
def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b
if __name__ == '__main__':
    number=input('输入一个分数:')
    number=number.split('/')
    num1=int(number[0])
    num2 = int(number[1])
    result=gcd(num1,num2)
    x=int(num1/result)
    y=int(num2/result)
    print(f"{str(x)}/{str(y)}")

