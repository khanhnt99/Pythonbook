import array as arr
number=arr.array('i',[1,3,5,7,9])
del number[2]
print(number)

'''
remove de xoa muc da cho
pop de xoa voi index cho truoc
'''

number.remove(1)
print(number)


print(number.pop(1))
print(number)
