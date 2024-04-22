cidadeA = 80000
cidadeB = 200000
anos = 0

while cidadeA < cidadeB:
    percentualA = cidadeA * 0.03
    cidadeA = cidadeA + percentualA
    percentualB = cidadeB * 0.015
    cidadeB = cidadeB + percentualB
    anos = anos + 1

print(f"Demorou {anos} anos para a cidade A se igualar a cidade B")