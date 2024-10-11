"""
Data manipulation with matrices
"""

def inicializa_matriz():
    matriz=[
        ["01", "Yolanda Martin",10,60000],
        ["02", "Roberto Perez",5,23000],
        ["03", "Paula Gonzalez",12,45000],
        ["04", "Omar Martinez",5,18000]
    ]
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