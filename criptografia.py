def rotacao(texto, giros):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_cifrado = ''

    for caractere in texto:
        if caractere.lower() in alfabeto:
            is_upper = caractere.isupper()
            index = alfabeto.index(caractere.lower())
            novo_index = (index + giros) % len(alfabeto)
            nova_letra = alfabeto[novo_index]
            if is_upper:
                nova_letra = nova_letra.upper()
            texto_cifrado += nova_letra
        else:
            texto_cifrado += caractere
    return texto_cifrado


texto = str(input('Digite seu texto: '))
giros = int(input('Quantas vezes vai rotar? '))


texto_rotacionado = rotacao(texto, giros)
print('Texto rotacionado:', texto_rotacionado)