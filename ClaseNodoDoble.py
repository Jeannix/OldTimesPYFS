#Clase Nodo con dos punteros 
class Nodo(object):
    def __init__(self,elemento):
        #Atributo que tendrá el Nodo - Puede tener más
        self.__elemento=elemento
        #Dos punteros que servirán para "unir" los Nodos
        #cuando se construya la lista. Siguiente y Anterior.
        self.__pSig = None
        self.__pAnt = None

    def getElemento(self):
        return self.__elemento
        
