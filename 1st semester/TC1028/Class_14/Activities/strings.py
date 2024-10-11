"""
El metodo split() divide la cadena en subcadenas si encuentra instancias del separador:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

El metodo strip() elimina cualquier espacio en blanco del principio o del final:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
"""

texto= '      Se bueno con los nerds, es muy probable que termines trabajando para uno de ellos'

texto2=texto.strip()
print(texto2)

textolist=texto2.split(" ")
print(textolist)

textolist[4]="Inteligentes"
print(textolist)

textolist2=" ".join(textolist)
print(textolist2)
for word in textolist2:
    print(word)