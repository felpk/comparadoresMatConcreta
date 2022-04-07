
import funcoes
import matplotlib.pyplot as plt

# PROGRAMA DE OUTPUT

contcs, contca = 0, 0
somacs = 0
somaca = 0

list_aleatorio = []
list_sequencial = []

for c in range(1, 100):
 
    listas = funcoes.geradora()
    funcoes.zeropraum(listas[0])

    cs = funcoes.csequencial(listas[0], listas[1])
    ca = funcoes.caleatorio(listas[0], listas[1])

    list_aleatorio.append(ca)
    list_sequencial.append(cs)
    
    if cs > ca:
        contcs += 1
 
    elif ca > cs:
        contca += 1
 
print('='*30)
print(f'Compar. Aleatorio  = {contca}')
print(f'Compar. Sequencial = {contcs}')
print('-'*30)

exp = []
for x in range(0,99):
    exp.append(x)

fig, (ax,ax_1) = plt.subplots(1,2)
plt.xlabel("número de simulações")
plt.ylabel("indices percorridos")
ax.scatter(exp,list_aleatorio,color = "red",label = "aleatorio")
ax.scatter(exp,list_sequencial,color = "blue",label = "sequencial")
ax_1.plot(exp,list_aleatorio,color = "red",label = "aleatorio")
ax_1.plot(exp,list_sequencial,color = "blue",label = "sequencial")
plt.legend()
ax.legend() 
plt.subplots_adjust(top = 2,right = 3.5)
plt.show()
