angka = int (input('Masukkan angka Fibonaci = ')) 

fibo = [0,1] 

for i in range (2,angka) :
    indek1 = fibo[i-2] 
    indek2 = fibo[i-1] 
    
    fibo2 = indek1 + indek2
    
    fibo.append(fibo2) 
    
print(fibo) 

 
