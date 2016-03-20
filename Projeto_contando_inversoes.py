'''Primerio passo importar a lista'''
import resource.py
lista = [line.rstrip('\n') for line in open('C:\\Users\\Samsung\\Downloads\\IntegerArray.txt')]
for i in range(0,len(lista)):
    lista[i]=int(lista[i]) 

'''Aplicando o algoritimo de inversão'''

def merge_grande(array):
    '''definindo um pivot'''
    meio=len(array)//2
    
    if len(array)<2:
        return(array)
    esquerda=array[:meio]
    print(esquerda)        #o que está acontecendo?
    direita=array[meio:]
    print(direita)         #o que está acontecendo?
    resultado=merge_pequeno(merge_grande(esquerda),merge_grande(direita))    
    print(resultado)      #o que está acontecendo?
    return(resultado)    

inversoes = 0    

def merge_pequeno(arrayE,arrayD):
    i=0
    j=0
    resposta=[]  
    global inversoes
    while i<len(arrayE) and j<len(arrayD):
        if arrayE[i]>arrayD[j]:
            print(arrayE)               #o que está acontecendo?
            resposta.append(arrayD[j])
            inversoes = inversoes + (len(arrayE) - i)
            j=j+1
        else: 
            resposta.append(arrayE[i])
            print(arrayE)              #o que está acontecendo?
            i=i+1
    '''Aqui tudo que foi separado fica organizado novamente'''    
    resposta.extend(arrayE[i:]) 
    resposta.extend(arrayD[j:])
        
    return(resposta)        

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
    
    
'''Fazendo um teste para verificar se está tudo funcionando '''

listateste=[2,3,1,1]
resposta_teste=merge_grande(listateste)
print(resposta_teste)
print(inversoes)

'''Fazendo para a lista gigantesca'''

resposta=merge_grande(lista)
print(resposta) #vemos que não dá certo porque a memória vai pro espaço!!!

'''tentando estratégias'''


    
