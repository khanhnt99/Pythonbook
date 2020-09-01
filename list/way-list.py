#append
QTM=[9,8,7,6,5,4]
print(QTM.append('hello'))

#extend: them tat ca cac phan tu list nay vao list khac
QTM2=['a','b','c','d']
QTM.extend(QTM2)
print(QTM)

#insert: Chen 1 phan tu vao index cho truoc
QTM.insert(1,'orange')
print(QTM)

#index(): Tra ve index cua phan tu phu hop dau tien
print(QTM.index('orange'))

#sort(): sap xep phan thu theo thu tu tang dan
numberlist=[1,2,4,3,5,6,8,9]
numberlist.sort()
print(numberlist)

#reverse(): dao nguoc phan tu lai trong list
numberlist.reverse()
print(numberlist)
