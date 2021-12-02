#nimed=["Anna", "Inna"]
#for i in range(3):
#    nimi=input("Sisesta nimi ")
#    nimed.append(nimi)
#print(nimed)
#nimed.sort()
#print(nimed)
#nimed.insert(1 ,input("Sisesta veel nimi "))
#print(nimed)
#nimed.remove("Anna")
#print(nimed)
#nimed.pop(2)
#print(nimed)
#print(len(nimed))
#nimed.count(nimed[0])
#№1
#Cities = ["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve"
#,"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa", "Hiiumaa", "Saaremaa"]
#while 1:
#    try:
#        Indeks = int(input("Введи почтовый индекс "))
#        if 10000<=Indeks<=99999:
#            break
#    except:
#        ValueError
#        print("Ошибка при наборе индекса")
#Indeks_1=Indeks//10000
#print(Cities[Indeks_1-1])
#if Cities[Indeks_1-1] == "Tallinn" or  Cities[Indeks_1-1] == "Narva, Narva-Jõesuu" or Cities[Indeks_1-1] == "Kohtla-Järve":
#    print("Оставайтесь дома!")
#else :
#    print("Носите маски!")
#№2
from random import *
#spisok=[]
#N=randint(2,20)
#for i in range(N):
#    spisok.append(randint(-50,50))
#print(spisok)
#while True:
#    try:
#        k=int(input("Что на что заменить? "))
#        if k<N//2:
#            break
#    except:
#        ValueError
#k-=1
#for i in range(k,-1,-1):
#    print(spisok[i],end="<->")
#    print(spisok[N-i-1])
#    A=spisok.pop(i)
#    spisok.insert(N-i-1-1,A)
#    B=spisok.pop(N-i-1)
#    spisok.insert(i,B)
#    print(spisok)
#№3
#spisok=[]
#N=randint(2,20)
#for i in range(N):
#    spisok.append(randint(-50,50))
#print(spisok)
#max=-50
#for element in spisok:
#    if element>max:
#        max= element
#print(max)
#Answer=max/len(spisok)
#print(Answer)
#A=spisok.index(max)
#spisok.pop(spisok.index(max))
#spisok.insert(A, round(Answer,2))
#print(spisok)
#№4
spisok=[]
N=randint(5,20)
for i in range(N):
    spisok.append(abs(randint(-50,50)))
print(spisok)
print(spisok.sort(reverse=True))
#№5
