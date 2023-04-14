numero = int(input())
var_map = list(map(int, input().split()))

media = sum(var_map) / numero

var_map.sort()

if numero % 2 == 0:
    mediana = (var_map[numero//2-1] + var_map[numero//2]) / 2
else:
    mediana = var_map[numero//2]
    
frequencia = {}
for num in var_map:
    frequencia[num] = frequencia.get(num, 0) + 1

moda = min([X for X, Y in frequencia.items() if Y == max(frequencia.values())])

print("{:.1f}".format(media))
print("{:.1f}".format(mediana))
print("{}".format(moda))