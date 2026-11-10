
# Katas 05 - Media de notas
lista_notas = [10, 5, 3, 4, 6, 2, 6]
def media_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        media_final = ("Aprobado", round(media, 2))
    else:
        media_final = ("Suspenso", round(media, 2))
    return media_final

print(media_notas(lista_notas))


# 



