import random
import time


def avancar():
    global carro1
    global carro2
    avanco = random.randint(0,1)

    temp = ""

    if avanco == 0:
        temp = carro1
        carro1 = "_" + f"{temp}"
        return carro1
    elif avanco == 1:
        temp = carro2
        carro2 = "_" + f"{temp}"
        return carro2
    
def verificacao():
    global carro1
    global carro2 
    global posicao

    if len(carro1) > 50 or len(carro2) > 50:
        posicao = 1
        imprimir_corrida()

def imprimir_corrida():
     global carro1
     global carro2
     print(" \n \n \n \n")
     print(carro1)
     print("="*60)
     print(carro2)

def corrida():
        imprimir_corrida()
        avancar()
        time.sleep(1)
        verificacao()


posicao = 0
carro1 = "civic"
carro2 = "corolla"

while posicao == 0:
    corrida()





