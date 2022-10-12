MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Aida nao pode tirar CNH")

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aula teorica apenas")
else:
    print("Nao pode tirar a CNH")
