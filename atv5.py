def inverter_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        nova_frase.append(palavra[::-1])

    return " ".join(nova_frase)


frase = input("Digite uma frase: ")

print("Frase invertida:", inverter_palavras(frase))
