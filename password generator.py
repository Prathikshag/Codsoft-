import random
n=['1','2','3','4','5','6','7','8','9','0','!','@','^','*','(',')',
   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
   ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

passw=[]
ip=int(input("Enter the length of the password:"))
for i in range (0,ip):
    passw.append(n[random.randint(0,71)])


print(''.join(map(str,passw)))
