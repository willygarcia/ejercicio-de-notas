notas = [ ] 
continuar = 1
while continuar == 1: 
	nota = str(input("ingrese la nota deseada: ")) 
	notas.append(nota) 
	continuar = int(input("Ingrese 1 para continuar y 0 para salir: "))

texto =("\n").join(notas)
f = open("notasguardadas.txt", "w") 
f.write(texto)  
f.close