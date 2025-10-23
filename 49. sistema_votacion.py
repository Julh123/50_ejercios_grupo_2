candidatos = {"A": 0, "B": 0, "C": 0}
for i in range(5):
    voto = input("Vote por A, B o C: ").upper()
    if voto in candidatos:
        candidatos[voto] += 1
print("Resultados:", candidatos)
ganador = max(candidatos, key=candidatos.get)
print("Ganador:", ganador)
