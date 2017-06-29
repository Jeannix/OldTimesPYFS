from random import *
import time

l=[]
for i in range(15):
    l.append(randrange(0,20))
    



def bBusca(L,e, inicio, fin):
	print(inicio,"::",fin)
	if inicio==fin:
		print("return L[inicio]==e :", L[inicio]==e)
		return L[inicio]==e
	i= inicio + (fin-inicio)//2
	print("corte: ",i)
	if L[i] == e:
		print("corte: True")
		return True
	elif L[i] > e:
		print("buscar izquierda")
		if inicio == i:
			return False
		else: 
			return bBusca(L,e,inicio,i-1)
	else:
		print("buscar derecha")
		return bBusca(L,e,i+1,fin)
		
def busca(L,e):
    if(len(L)==0):
        return False
    return bBusca(L,e,0,len(L)-1)
    
    
def buscasec(L,e):
    for i in range(0,len(L)):
        if L[i]==e:
            return True
    return False

start_time = time.time()
l7=busca(l,len(l))
end_time = time.time() - start_time
print "BusquedaBi demoro:",end_time
start_time=time.time()
l.sort()
l8=busca(l,len(l))
end_time=time.time()-start_time
print "BusquedaBi con lista ordenada demoro:",end_time


#Busqueda secuencial
start_time = time.time()
l9=buscasec(l,len(l))
end_time = time.time() - start_time
print "Busqueda demoro:",end_time
start_time=time.time()
l.sort()
l10=buscasec(l,len(l))
end_time=time.time()-start_time
print "Busqueda con lista ordenada demoro:",end_time

    
