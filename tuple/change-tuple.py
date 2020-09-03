'''
Tuple khong the bi thay doi
Nhung ban than phan tu cua tuple la 1 kieu du lieu co the thay doi thi ta thay doi duoc
Ta co the gan gia tri khac cho tuple (gan lai-reassignment)
'''

my_tuple=(1,3,5,[7,9])

my_tuple[3][0]=8
print(my_tuple)

my_tuple=(1,2,3,4,5,6,7,8,9)
print(my_tuple)

print((2,4,6)+(3,5,7))
print(("Quan tri mang",)*3)
