dict2 = {1:'quantrimang.com','quantrimang':'Cong nghe'}

#cap nhat gia tri

dict2['quantrimang']='Quan tri mang'

print(dict2)

dict2[2]='Python'
print(dict2)

# xoa phan tu cua dict

binh_phuong = {1:1,2:4,3:9,4:16,5:25}

print(binh_phuong.pop(4))
print(binh_phuong)

# xoa phan tu cu the
del binh_phuong[2]
print(binh_phuong)

#xoa phan tu bat ki
print(binh_phuong.popitem())
print(binh_phuong)

