idade_em_dias = int(input("Digite a idade em dias: "))

anos = idade_em_dias // 365
dias_restantes = idade_em_dias % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s).")