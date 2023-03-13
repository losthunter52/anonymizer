import random

def test(
        #obrigatorio
        data,
        fields,
        #obrigatorio um dos dois
        salto = 25,
        vetor = [30, 23],
        #nao obrigatorio
        numero = -1
):
    # tira o resto da divisao por 2 do numero
    aux = numero - (numero % 2)
    # divide o numero por 2 (o resultado aqui será um inteiro)
    aux = aux / 2
    # multiplica o salto por aux para saber o quanto o valor pode variar para cima ou para baixo
    variancia = salto * aux
    # vetor vazio
    vetor = []
    #log vazio
    log = ""
    # preenche o vetor com numeros aleatorios de acordo com o salto e a variancia
    for i in range(numero):
        x = random.randint(-variancia, variancia)
        vetor.append(x)
    # atribui um numero aleatorio para cada registro do banco e adiciona esse numero a variavel log
    # criando uma chave que pode ser utilizada depois para reter o dado
    # soma o valor real com o valor do vetor na posição numero 
    for i in range(len(data)):
        for field in fields:
            r = random.randint(1, numero)
            log = log + str(r)
            data[i][field] = data[i][field] + vetor[r]
    # retorna a chave o vetor e a database com variancia
    return {"log": log, "vetor": vetor, "database": data}