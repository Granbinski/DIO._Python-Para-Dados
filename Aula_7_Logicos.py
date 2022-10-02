saldo = 1000
saque = 200
limite = 100
saldo >= saque
saque <= limite
saldo >= saque and saque <= limite
saldo >= saque or saque <= limite

not 1000 > 1500
not " saque 1500 ; "
not ""
conta_especial = True
saldo >= saque and saque <= limite or conta_especial and saldo >= saque
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
