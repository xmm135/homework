def normalize1(name):
    return name[0].upper() + name[1:].lower()


def normalize2(name):
    str1 = ''

    for i, n in enumerate(name):
        if i == 0:
            str1 += n.upper()
        else:
            str1 += n.lower()
    return str1


L1 = ['admin', 'LISA', 'barT']
print("切片实现")
L2 = list(map(normalize1, L1))
print(L2)
print("enumerate： 枚举字符串实现")
print(list(map(normalize2, L1)))


num_list = []
num = input("Please enter the name of digits:")
for i in range(int(num)):
    N = input("please enter name:")
    num_list.append(str(N))
LL2 = list(map(normalize1, num_list))
print(LL2)
for nums in LL2:
    print(nums, )


if __name__ == '__main__':
    pass