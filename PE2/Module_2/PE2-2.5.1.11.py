str1 = input("Enter string 1 with numbers from 1 to 9: ")
str2 = input("Enter string 2 with numbers from 1 to 9: ")
str3 = input("Enter string 3 with numbers from 1 to 9: ")
str4 = input("Enter string 4 with numbers from 1 to 9: ")
str5 = input("Enter string 5 with numbers from 1 to 9: ")
str6 = input("Enter string 6 with numbers from 1 to 9: ")
str7 = input("Enter string 7 with numbers from 1 to 9: ")
str8 = input("Enter string 8 with numbers from 1 to 9: ")
str9 = input("Enter string 9 with numbers from 1 to 9: ")

lst1 = list(str1)
lst2 = list(str2)
lst3 = list(str3)
lst4 = list(str4)
lst5 = list(str5)
lst6 = list(str6)
lst7 = list(str7)
lst8 = list(str8)
lst9 = list(str9)

colm1 = [lst1[0],lst2[0],lst3[0],lst4[0],lst5[0],lst6[0],lst7[0],lst8[0],lst9[0],]
colm2 = [lst1[1],lst2[1],lst3[1],lst4[1],lst5[1],lst6[1],lst7[1],lst8[1],lst9[1],]
colm3 = [lst1[2],lst2[2],lst3[2],lst4[2],lst5[2],lst6[2],lst7[2],lst8[2],lst9[2],]
colm4 = [lst1[3],lst2[3],lst3[3],lst4[3],lst5[3],lst6[3],lst7[3],lst8[3],lst9[3],]
colm5 = [lst1[4],lst2[4],lst3[4],lst4[4],lst5[4],lst6[4],lst7[4],lst8[4],lst9[4],]
colm6 = [lst1[5],lst2[5],lst3[5],lst4[5],lst5[5],lst6[5],lst7[5],lst8[5],lst9[5],]
colm7 = [lst1[6],lst2[6],lst3[6],lst4[6],lst5[6],lst6[6],lst7[6],lst8[6],lst9[6],]
colm8 = [lst1[7],lst2[7],lst3[7],lst4[7],lst5[7],lst6[7],lst7[7],lst8[7],lst9[7],]
colm9 = [lst1[8],lst2[8],lst3[8],lst4[8],lst5[8],lst6[8],lst7[8],lst8[8],lst9[8],]

sqr1 = [lst1[0],lst1[1],lst1[2],lst2[0],lst2[1],lst2[2],lst3[0],lst3[1],lst3[2]]
sqr2 = [lst1[3],lst1[4],lst1[5],lst2[3],lst2[4],lst2[5],lst3[3],lst3[4],lst3[5]]
sqr3 = [lst1[6],lst1[7],lst1[8],lst2[6],lst2[7],lst2[8],lst3[6],lst3[7],lst3[8]]
sqr4 = [lst4[0],lst4[1],lst4[2],lst5[0],lst5[1],lst5[2],lst6[0],lst6[1],lst6[2]]
sqr5 = [lst4[3],lst4[4],lst4[5],lst5[3],lst5[4],lst5[5],lst6[3],lst6[4],lst6[5]]
sqr6 = [lst4[6],lst4[7],lst4[8],lst5[6],lst5[7],lst5[8],lst6[6],lst6[7],lst6[8]]
sqr7 = [lst7[0],lst7[1],lst7[2],lst8[0],lst8[1],lst8[2],lst9[0],lst9[1],lst9[2]]
sqr8 = [lst7[3],lst7[4],lst7[5],lst8[3],lst8[4],lst8[5],lst9[3],lst9[4],lst9[5]]
sqr9 = [lst7[6],lst7[7],lst7[8],lst8[6],lst8[7],lst8[8],lst9[6],lst9[7],lst9[8]]

sample_list = ['1','2','3','4','5','6','7','8','9']

BIG = [str1,str2,str3,str4,str5,str6,str7,str8,str9,colm1,colm2,colm3,colm4,colm5,colm6,colm7,colm8,colm9,sqr1,sqr2,sqr3,sqr4,sqr5,sqr6,sqr7,sqr8,sqr9]

Sum_check = 0

for i in BIG:
    for j in sample_list:
        if j in i:
            Sum_check += 1
        else:
            continue    

if Sum_check == 243:
    print("Yes")
else:
    print("No")