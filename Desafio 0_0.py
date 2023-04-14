
#leitor de valores de entrada
numero = int(input('Insira o número de elementos: '))
var_map = list(map(int, input('Insira os elementos separados por espaço: ').split()))

1
#calculando a média
media = sum(var_map) / numero

#ordenando a array
var_map.sort()

#calculando a mediana
if numero % 2 == 0:
    mediana = (var_map[numero//2-1] + var_map[numero//2]) // 2
else:
    mediana = var_map[numero//2] 
    
    # // é utilizado para obtenção de Indices dos valores do centro da Array
    
    
#Calculando a moda
frequencia = {} #dicionário para contabilizar frequencia dos elementos
for num in var_map:
    frequencia[num] = frequencia.get(num, 0) + 1
    #Min escolhendo a moda numericamente menor
    #Max localizar chaves de valor máximo em lista
moda = min([X for X, Y in frequencia.items() if Y == max(frequencia.values())]) 

#Realizando Outputs ddo desafio
    #Outputs em format para arredondar para casa decimal
print("A média é: {:.1f}".format(media))
print("A mediana é: {:.1f}".format(mediana))
print("A moda é: {}".format(moda))