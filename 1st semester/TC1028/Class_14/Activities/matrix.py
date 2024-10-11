"""
Data manipulation with matrices
"""

def inicializa_matriz():
    matriz=open("1st semester/TC1028/Class_14/Activities/alumni.txt","a")

    # Put data in
    matriz.write("Andrea\n")
    matriz.write("Ernesto\n")
    matriz.write("Carlos\n")
    matriz.write("Bauer\n")

    return matriz

def imprime_matriz(matriz):
    print()
    print("ID\t\tNombre\t\tAntiguedad\t\tSueldo")
    for lista in matriz:
        print("\t")
        for valor in lista:
            print(valor, end="\t\t")
        print()

def aumenta_sueldo(matriz):
     for i in range(len(matriz)):
        if matriz [i][2]>=10:
            matriz[i][3]=round(matriz[i][3]*1.1)
        return matriz

def main():
    m=inicializa_matriz()
    imprime_matriz(m)
    m_aumento=aumenta_sueldo(m)
    imprime_matriz(m_aumento)

main()