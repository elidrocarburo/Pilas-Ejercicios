Torre_inicial= [3,2,1]
Torre2= []
Torre3= []

def mover_torre(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.pop()
        destino.append(disco)
        print(f"Mover disco {disco} de {origen} a {destino}")
    else:
        mover_torre(n - 1, origen, auxiliar, destino)
        mover_torre(1, origen, destino, auxiliar)
        mover_torre(n - 1, auxiliar, destino, origen)

mover_torre(len(Torre_inicial), Torre_inicial, Torre3, Torre2)

print("Estado final de las torres:")
print("Torre inicial:", Torre_inicial)
print("Torre 2 (auxiliar):", Torre2)
print("Torre 3 (destino):", Torre3)