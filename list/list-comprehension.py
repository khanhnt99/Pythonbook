''' Bieu thuc di kem voi lenh for duoc dat trong dau []'''
cub3=[3**x for x in range(9)]

print(cub3)

'''
cub3=[]
 for x in range(9);
	cub3.append(3**x)
	print(cub3)
'''

cub4=[3**x for x in range(9) if x>4]
print(cub4)

so_le= [x for x in range(18) if x%2==1]
print(so_le)

noi_list=[x+y for x in ['Ngon ngu ','Lap trinh '] for y in ['C++','Python']]
print(noi_list)

for ngon_ngu in ['Python','Java','C']:
	print("Toi thich lap trinh",ngon_ngu)
