'''
Thay doi 1 phan tu trong mang
'''
import array as arr
numbers=arr.array('i',[1,2,3,4,5])
numbers[0]=0
print(numbers)

'''
Them phan tu trong mang su dung
append() extend()
'''
number1=arr.array('i',[3,5,7])
number1.append(4)
print(number1)

number1.extend([8,9,10])
print(number1)

'''
toan tu +
'''

mang_le = arr.array('i',[3,5,7])
mang_chan=arr.array('i',[2,4,6,8])
number2=mang_le + mang_chan)
print(number2)
