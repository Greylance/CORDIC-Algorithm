#Algoritma untuk menghitung sin dan cos dengan input derajat
#Hanya berlaku untuk derajat pada Kuadran I
#Program ini hanya untuk sekedar demonstrasi, tidak untuk diimplementasikan
import numpy as np
a = [-1,1] #variabel arah
sd = float(input("Masukan derajat:"))
while(sd>360):
    sd = sd - 360
m_rotasi = np.matrix([[1,-1],[1,1]])
#while(True):
if(sd>0):
    sd = sd - np.arctan(2**(0))*180/np.pi
elif(sd<0):
    sd = sd + np.arctan(2**(0))*180/np.pi
#elif(sd == 0):
i = 1
#for i in range(12):
while(True):
    print(i)
    #i = 1
    if(sd > -0.005 and sd < 0.005):
        break
    elif(sd == 0):
        break
    elif(sd>0):
        sd = sd - np.arctan(2**(-i))*180/np.pi
        m_rotasi = m_rotasi*np.matrix([[1,(-2**(-i))*a[1]],[(2**(-i))*a[1],1]])
    elif(sd<0):
        sd = sd + np.arctan(2**(-i))*180/np.pi
        m_rotasi = m_rotasi*np.matrix([[1,(-2**(-i))*a[0]],[(2**(-i))*a[0],1]])
    i = i + 1
    print(m_rotasi)
    print(sd)
#calculate K constant
K = 1
for k in range(i):
    d = np.arctan(2**(-k))
    K = K * np.cos(d)
    #print(K)
x,y = K*m_rotasi*np.matrix([[1],[0]])
print("Nilai cos =", x[0])
print("Nilai sin =", y[0])