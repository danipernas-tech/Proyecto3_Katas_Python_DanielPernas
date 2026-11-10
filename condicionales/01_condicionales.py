
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

lista_notas = [10, 5, 3, 4, 6, 2, 6]
def media_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        media_final = ("Aprobado", round(media, 2))
    else:
        media_final = ("Suspenso", round(media, 2))
    return media_final

print(media_notas(lista_notas))


# 7. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

hora = int(input("Que hora es?"))
if hora < 0 or hora > 23:
    print("Horario incorrecto")
elif hora >= 20:
    print("Es de noche")
elif hora >= 12:
    print("Es de tarde")
elif hora >= 8:
    print("Es de mañana")
else:
    print("Es de noche")


