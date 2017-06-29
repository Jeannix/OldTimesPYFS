def mezclar(l1,l2):
    mezcla = []
    for i in range(0,len(l1)):
            mezcla.append(l1[i])
            mezcla.append(l2[i])
    return mezcla

lista1=[1,3,5]
lista2 = [2,4,6]
print "Mezclar ",lista1," con ",lista2," = ",mezclar(lista1,lista2)


def multiplicar(l1,l2):
    for i in range(0, len(l1)):
        for j in range(0,len(l2)):
            l1[i] *= l2[j]
    return l1


lista1=[2,3,4]
lista2 = [4,5]
print "El resultado de la multiplicar ", lista1, " y ", lista2, " = ",multiplicar(lista1,lista2)


def multiplicar2(l1,l2):
    multi = 1
    for i in range(0,len(l2)):
        multi*=l2[i]
    for i in range(0,len(l1)):
        l1[i]*=multi
    return l1

lista1=[2,3,4]
lista2 = [4,5]
print "El resultado de la multiplicar ", lista1, " y ", lista2, " = ",multiplicar2(lista1,lista2)

def extraer(lista, limite):
    res = []
    for i in range(0,len(lista)):
        if lista[i]<=limite:
            res.append(lista[i])
    return res

l=[4,50,13,12,30]
limite=13
print "el resultado de la extracion de lista : ", l, " y  limite :", limite, " es ",extraer(l,limite)
