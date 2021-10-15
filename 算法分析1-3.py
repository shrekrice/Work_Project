def zqq(num):
    f_num=[]
    while num%100!=0 &num%100>=0:
         s_num=int(num%100)
         f_num.append(s_num)
         num=int(num/100)
    return f_num
if __name__ == '__main__':
    number=input('请输入一个整数：')
    l_number=zqq(int(number))
    result=sum(l_number)
    if result/11==0:
        print(f"{number}能被11整除！")
    else:
        print(f"{number}不能被11整除！")
