import random

seq =[["!","#","$","%","&","'","(",")","*","+","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["0","1","2","3","4","5","6","7","8","9"]]
n=int(input("Give the length of the password"))
for i in range(10):
    password=[]
    for j in range(n):
        password.append(random.choice(seq[j%4]))
    pwd=''.join(password)
    print(pwd)