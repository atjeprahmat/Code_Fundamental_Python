#BELAJAR PYTHON
"""BELAJAR PYTHON"""



a = 1
b = 2
c = 'Selamat Datang di'
d = "SMK Wikrama"
e = "Bogor"

#Selamat Datang di SMK Wikrama 2 Bogor
print(c, d, b, e)
#Hasil dari 1+2=3

print("Hasil dari", a, "+",  b, "=", a+b)















print(c, d, a*b)






#tipe data bilangan (bulat/integer dan float)
#bulat/integer
x = 7
print(x)

y = 7.0
print(y)
print(x+y)


#operator
print("-----------operator----------")
print(10+2)
print(12*2)
print(8/5)
print(14-1)
print(2**2)
print(5%2)

print("-----------operator menggunakan variabel----------")
a1 = 5
a2 = 6
print(a1+a2)
print(a1*a2)
print(a2-a1)
print(a1/a2)




print("-----------pengelompokan operasi----------")
print(2+2*4) #operasi perkalian akan di lakukan terlebih dahulu 10
print((2+2)*4) #tanda kurung menandakan operasi yang didahulukan
print((4/2)*5)






print("----pembulatan----")
b1 = 14.8
b2 = 18.4
print(int (b1))  #int pembulatan ke bawah
print(round(b2)) #round pembulatan ke atas jika > 5, ke bawah jika <= 5





print("---------tipe data string---------")
print('SMK Wikrama Bogor') #string menggunakan kutip 1 atau kutip 2
print("SMK Wikrama Bogor")







print("doesn't")
print('doesn\'t')
print('i cant wait')
print('i can\'t wait')
print("i can't wait")








print("""SMK Wikrama Bogor
Jl. Raya Wangun Kel. Sindangsari
Kec. Bogor Timur Kota Bogor""")   #kutip 3 bisa digunakan untuk string untuk kondisi beberapa baris

#print("SMK Wikrama Bogor
#Jl. Raya Wangun Kel. Sindangsari
#Kec. Bogor Timur Kota Bogor")



print("---menggabungkan string menggunakan (+)---")
c1 = "SMK"
c2 = "Wikrama"
c3 = "Bogor"
c4 = c1+c2+c3
c5 = c1+' '+c2+' '+c3
print(c4)
print(c5)
print(c1+' '+c2+' '+c3)







print("---menggabungkan angka menggunakan (+)---")
d1 = 1
d2 = 2
d3 = 3
d4 = d1+d2+d3

print(d4)
print(str(d1)+str(d2)+str(d3))
print(str(d1)+'+'+str(d2)+'+'+str(d3))
print(str(d1)+'+'+str(d2)+'+'+str(d3)+'='+str(d4))

print("---Array/List/Larik---")
a = [1,2,3,4,5]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[0],a[1],a[2],a[3],a[4])

e1 = ['Wikrama', 1, 'Bogor']
print(e1[0], e1[1], e1[2])

print("--menghitung jumlah elemen pada array--")
print("jumlah elemen pada array adalah", len(e1))

