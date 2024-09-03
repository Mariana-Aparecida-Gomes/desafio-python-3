def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

resultado = contar_vogais("Programacao")
print(resultado)  # Saída: 5