'''
Lenh break co the duoc su dung de dung vong lap for
Khi do lenh else duoc bo qua
Phan else trong for se chay khi khong co break duoc thuc thi 
'''

#lap tu 0 den 10
for num in range(0,10):
	for i in range(2,num):
		if num%i==0:
	  		j=num/i
 	  		print ('%d=%d*%d' %(num,i,j)) 
#dung vong for hien tai, chuyen den so tiep theo trong vong for hien tai
          		break
  	else:
		print(num,'la so nguyen to')

