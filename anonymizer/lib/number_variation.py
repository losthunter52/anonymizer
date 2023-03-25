import random

def var_num_data(data, fields, variacao):
    def var_num(valor_original, variacao):
        if valor_original > 0 and isinstance(valor_original, int):
            return valor_original + random.randint(-variacao, variacao)
        else:
            return valor_original + random.uniform(-variacao, variacao)
        
    for i in range(len(data)):
        for field in fields:
            valor_original = data[i][field]
            if isinstance(valor_original, str) and valor_original.isdigit():
                valor_original = int(valor_original)
                data[i][field] = var_num(valor_original, variacao)
            elif isinstance(valor_original, (int, float)):
                novo_valor = var_num(valor_original, variacao)
                if isinstance(novo_valor, float):
                    novo_valor = round(novo_valor, 3)
                data[i][field] = novo_valor
    return data


def var_num_random_data(data, fields,numero,salto):
    print("rodou denovo")
    def var_num(valor_original, vetor_aleatorio):
        if valor_original > 0 and isinstance(valor_original, int):
            while True:
                indice = random.randint(0, len(vetor_aleatorio) - 1)
                valor_escolido = vetor_aleatorio[indice]
                anonymized= (valor_original + random.randint(-valor_escolido,valor_escolido))
                if anonymized != valor_original:
                    break
            print("Valor origial",valor_original, "Anonimizado", anonymized, "vetor:", vetor_aleatorio, "indice:", indice)
            return anonymized
        else:
            while True:
                indice = random.randint(0, len(vetor_aleatorio) - 1)
                valor_escolido = vetor_aleatorio[indice]
                anonymized = (valor_original + random.uniform(-valor_escolido, valor_escolido))
                if anonymized != valor_original:
                    break
            print("Valor origial",valor_original,"Anonimizado", anonymized, "vetor:", vetor_aleatorio, "indice:", indice)
            return anonymized

        
    aux = numero // 2
    variancia = salto * aux
    numeros_unicos = []
    while len(numeros_unicos) < numero:
        x = random.randint(-variancia, variancia)
        if x != 0 and x not in numeros_unicos:
            numeros_unicos.append(x)

    vetor_aleatorio = [abs(x) for x in numeros_unicos]
    
    for i in range(len(data)):
        for field in fields:
            valor_original = data[i][field]
            if isinstance(valor_original, str) and valor_original.isdigit():
                valor_original = int(valor_original)
                data[i][field] = var_num(valor_original,vetor_aleatorio)
            elif isinstance(valor_original, (int, float)):
                novo_valor = var_num(valor_original,vetor_aleatorio)
                if isinstance(novo_valor, float):
                    novo_valor = round(novo_valor, 3)
                data[i][field] = novo_valor
    return data
