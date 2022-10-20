import os,sys


def info(file):
    consonants = "bcdfghjklmnpqrstvwxyz"
    countc =0
    countv=0
    array = [0,0,0,0,0,0,0,0,0,0]
    f = open(file) # open file
    print(file+"\n") #name file
    x=len(f.read())
    print("1. Всего символов -->"+str(x)+"\n") #count char
    lists = [line.strip() for line in open(file)] # all word in array
    word="" #max length word
    lenv=0 #max length
    wordm="" #min length word
    lenvm=11 #min length
    for i in lists:
        for j in i: 
            if j.lower() in consonants: countc+=1
            else: countv+=1
        if len(i)>lenv: #search max
            word = i
            lenv= len(i)
        if len(i)<lenv: #search min
            wordm=i
            lenvm=len(i)
        array[len(i)-1] = array[len(i)-1]+1
    print("2. Максимальная длина слова -->" + str(lenv)+"\n")
    print("3. Минимальная длина слова --> "+ str(lenvm)+"\n")
    print("4. Средняя длина слова -->"+str(round(x/len(lists))))
    print("5. Количество гласных -->" + str(countv)+"\n")
    print("6. Количество согласных -->" + str(countc) + "\n")
    print("7. Количество повторений слов с одинаковой длиной:\n\n")
    for i in range(1,11):
        print("* "+str(i)+" сим. >> "+str(array[i-1])+" повтор.")
    f.close()
    

for file in os.listdir(r"C:\Users\ReyLpol\Desktop\DevPython\PythonApplication1\PythonApplication1"):
    info(file)


