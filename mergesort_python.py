'''CÓDIGO RETIRADO DA INTERNET PARA ESTUDO
SITE : http://interactivepython.org'''
 
def mergeSort(vetor):
    if len(vetor)>1:
        i=0
        j=0
        k=0
        mid = len(vetor)//2
        '''Dividindo o vetor'''
        esquerda = vetor[:mid]
        direita = vetor[mid:]
        '''Chamando a função'''
        mergeSort(esquerda)
        mergeSort(direita)
        
        '''Organizando os vetores quebrados'''
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i=i+1
            else:
                vetor[k]=direita[j]
                j=j+1
            k=k+1
           
        while i < len(esquerda):
            vetor[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            vetor[k]=direita[j]
            j=j+1
            k=k+1
            
    return(vetor)            
    
'''Fazendo o teste para ver se funciona '''
vetor = [1,5,3,2,4,6,7,1,2,3,9,0,11,23,22,21,54,67,87,78,76,74,23,21]
print(mergeSort(vetor))




