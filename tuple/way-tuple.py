QTM=('a','b','c','d','e','f','g','h',1,2,3,4,5,6)

print(QTM.count('a'))

print(QTM.index('b'))

# all() tra ve gia tri true neu tat ca phan tu tuple la true hoac tuple rong
print(all(QTM))

# any() tra ve gia tri true neu tat ca phan tu tuple la dung va false neu tuple rong
QTM1=()
print(any(QTM1))

# vong lap for trong tuple
for ngon_ngu in ('Python','C++','Wed'):
	print('Toi thich lap trinh',ngon_ngu)
