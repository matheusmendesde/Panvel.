def teste(rex, bob, oli):
    if oli > rex:
        pos = oli - rex
        
    else:
        pos = rex - oli
        
    if oli > bob:
        pos2 = oli - bob
    else:
        pos2 = bob - oli

    if pos == pos2:
        return 'Bob e Rex chegaram ao mesmo tempo, portanto, Oli conseguira fugir'
    elif pos < pos2:
        return 'Rex pegara o gato'
    else:
        return 'Bob pegara o gato'
    
def validacao(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("Por favor, insira um número inteiro positivo.")

rex = validacao('Qual a posiçao do Rex: ')
bob = validacao('Qual a posiçao do Bob: ')
oli = validacao('Qual a posiçao do Oli: ')

resultado = teste(rex, bob, oli)
print(resultado)