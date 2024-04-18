import numpy as np
import copy
from random import randint

def numerical(x): #turn text into number
    numbers=[]
    for i in x.lower():
        num= ord(i)- 96
        if num== -64:
            num+=64
        else:
            pass
        numbers.append([num])
    return numbers

def alphabet(x): #number into letter
    letters=[]
    for i in x:
        if int(i)!=0:
            letter=chr(int(i)+64)
        else:
            letter=' '
        letters.append(letter)
    return letters

def matrix_mult(x,y): #multiply matix
    mat = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]
    return mat

def matrix_add(x,y): #add matrix
    mat = [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
    return mat

def matrix_sub(x,y): #subtract matrix
    mat = [[x[i][j] - y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
    return mat

def matrix_inv(x): #inverse matrix
    x = np.array(x)
    mat = np.linalg.inv(x)
    mat = mat.tolist()
    return mat

def matrix_inv2(x):
    d=x[0][0]*x[1][1] - x[0][1]*x[1][0]
    return ([[x[1][1]/d, -x[0][1]/d], 
                [-x[1][0]/d, x[0][0]/d]])

######################################################################

print("Welcome to the Affine Cipher app")
print()
while True:
    check=0
    det=0
    kapital=[]
    alpha=[]
    word=input('Please type the sentence you would like to encrypt:')

    while check==0: #Check input
        wordcheck=word.replace(" ", "")
        if wordcheck.isalpha():
            check+=1
        else:
            word=input("Only letters are allowed:")
        
    len_word=len(word)

    for i in word: #Check capitalization
        if i==' ':
            kapital.append(1)
        elif i.isupper():
            kapital.append(1)
        else:
            kapital.append(0)
            
            
    mat_word=(numerical(word))
    vec_enkr=[[randint(0,10)] for j in range(len_word)]
    
    while True:
        mat_enkr=[[randint(0,10) for j in range(len_word)]for i in range(len_word)]
        enkr=np.array(mat_enkr)
        det=int(np.linalg.det(enkr))
        if abs(det)==1:
            break

    enkripsi=(matrix_mult(mat_enkr,mat_word)) #encyption
    enkripsi=matrix_add(enkripsi,vec_enkr)

    for i in range(len_word): #mod all element
        for j in range(1):
            if (enkripsi[i][j]%26)==0:
                alpha.append(26)
            else:
                alpha.append(enkripsi[i][j]%26)

    alpha=alphabet(alpha)

    for i in range(len_word): #Uppercase, Lowercase
        if kapital[i]==0:
            (alpha[i])=(alpha[i]).lower()
        else:
            (alpha[i])=(alpha[i]).upper()

    print()
    print('Hasil enkripsi:',"".join(alpha))
    print()

    print("Matriks enkripsi:")
    for i in range(len_word): # print matriks
        for j in range (len_word):
            if mat_enkr[i][j]>9:
                print(mat_enkr[i][j],end=' ')
            else:
                print('',mat_enkr[i][j],end=' ')
        print()
    print()

    print("Vektor enkripsi:")
    for i in range(len_word): #print vector
        for j in range (1):
            print(vec_enkr[i][j],end=' ')
        print()
    print()

    ####Option####

    option=input('''Do you want to encrypt this sentence?
        1. Yes
        0. No
        Your choice:''')

    check=0  #Check input
    while check==0:
        if option=='0' or option=='1':
            check=+1
        else:
            option=input("Type number 1 or 0:")

    if option=='1':
        
        vec_dek=copy.deepcopy(vec_enkr)
        mat_dek=matrix_inv(mat_enkr)
        
        for i in range(len_word): #mod inverse matriks enkripsi
            for j in range(len_word):
                mat_dek[i][j]=(mat_dek[i][j]%27)

        for i in range(len_word): #Decryption Vector
            for j in range (1):
                if vec_dek[i][j]!=0:
                    vec_dek[i][j]=(27-vec_enkr[i][j])

        print() #print words
        print('Decryption Result:',word)
        print()

        print("Decryption Matrix:")
        for i in range(len_word): # print Decryption matrix
            for j in range(len_word):
                if int(mat_dek[i][j])>9:
                    print("{:.1f}".format(mat_dek[i][j]),end=' ')
                else:
                    print('',"{:.1f}".format(mat_dek[i][j]),end=' ')
            print()
        print()

        print("Decryption Vector:")
        for i in range(len_word): #print Decryption Vector
            for j in range (1):
                print(vec_dek[i][j],end=' ')
            print()
        print()

    while True:
        print()
        restart=input('''Do you want to encrypt another sentence?
    1. Yes
    0. No
    Pilihan anda:''')
        if restart=='1' or restart=='0':
            break
        print("Input have to be 0 or 1")

    if restart=='1':
        continue
    else:
        print()
        print("Thankyou for using this application")
        print()
        break
            




        






