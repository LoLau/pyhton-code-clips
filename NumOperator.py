__author__ = 'lg'


def sum_num(li):
    sum1 = 0
    for i in li:
        sum1 += i
    print('the sum is:%d' % sum1)


def aver_num(li):
    sum1 = 0
    for i in li:
        sum1 += i
    aver = float(sum1)/len(li)
    print('the average is:%.2f' % aver)


def main():
    str1 = '''
        (1)get sum of the 5 numbers
        (2)get average of the 5 numbers
        (X)exit'''
    list1 = [2, 3, 4, 5, 5]
    print(str1)
    in_put = -1
    while True:
        in_put = input('slect the number:')
        if in_put == '1':
            sum_num(list1)
        elif in_put == '2':
            aver_num(list1)
        elif in_put == 'X':
            break
        else:
            print('input error')

if __name__ == '__main__':
    main()
