from PIL import Image
from matplotlib import pyplot
from tkinter.filedialog import askopenfilename
import time

"""
	Converte de decimal a binario, se define de cuantos bits
"""
def decimalToBin(num, n):
	temp=format(num, 'b')
	espacio= "0"
	if (n-len(temp))>=0:
		espacio*=(n-len(temp))
		temp=espacio+temp
	return temp[len(temp)-n:]

"""
	Se usa para tomar la la ruta y el nombre del archivo
"""
def getRuta(ruta):
	temp=""
	for letra in ruta:
		if(letra=="."):
			break
		else:
			temp+=letra
	return temp

"""
	Guarda datos en un archivo
"""
def writeImage(datos, ruta):
	f= open(ruta,"w+")
	for i in range(len(datos)):
		f.write("%s\n" % datos[i])
	return True

try:
	filename = askopenfilename()
	im = Image.open(filename)
	pix = im.load()
	ancho, alto = (im.size)
	if( ancho == 320 and alto == 240 ):

		inicio = int(round(time.time() * 1000))
		imagen1D=[] # simula la memoria

		for y in range(0, alto):
			for x in range(0, ancho):
				temp=[0,pix[x,y][0],pix[x,y][1],pix[x,y][2]] # un pad para que quepa en 32 bits
				imagen1D.append(temp)

		for i in range(len(imagen1D)):
			imagen1D[i]=decimalToBin(imagen1D[i][0],8)+decimalToBin(imagen1D[i][1],8)+decimalToBin(imagen1D[i][2],8)+decimalToBin(imagen1D[i][3],8) # convierte a binario

		ruta=getRuta(filename)+".bin"
		writeImage(imagen1D, ruta)
		fin = int(round(time.time() * 1000))
		cronometro=fin-inicio
		print(">> Conversion completa, tiempo transcurrido %d ms" % cronometro)
	else:
		print(">> La imagen no es 320x240")
except:
	print(">> La imagen no pudo ser cargada correctamente")