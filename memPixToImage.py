from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageOps
import time

"""
	Carga una imagen en binario 
"""
def openImagen(ruta):
	temp=[]
	f=open(ruta, "r")
	fl =f.readlines()
	for x in fl:
		temp.append(x[:len(x)-1])
	return temp

"""
	Guarda binario desde archivo
"""
def writeImage(datos, ruta):
	f= open(ruta,"w+")
	for i in range(len(datos)):
		f.write("%s\n" % datos[i])
	return True

"""
	Calcula el promedio de una tupla / pixel rgb
"""
def getProm(tupla):
	temp=0
	for ele in tupla:
		temp+=ele
	return temp//3
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
	Convierte una imagen a mem pix (1 bit)
"""
def toMemPix():
	filename = askopenfilename()
	im = Image.open(filename)
	pix = im.load()
	ancho, alto = (im.size)
	pix=im.load()
	print(im.size)
	mem=[]
	umbral=155
	for j in range(0, alto):
		temp=""
		for i in range (0, ancho):
			prom=getProm(pix[i,j])
			if prom<umbral:
				tempPix="00"
				tempPix+=temp
				temp=tempPix
			else:
				tempPix="01"
				tempPix+=temp
				temp=tempPix
		mem.append(temp)

	ruta=getRuta(filename)+"_mem_pix.bin"
	writeImage(mem, ruta)

#toMemPix() #para hacer un archivo de umbralizacion de prueba

try:
	ancho,alto=(320, 240);
	img = Image.new('RGB', (ancho,alto), color = 'red') # imagen base
	pix=img.load()
	filename = askopenfilename()
	memPix=openImagen(filename)
	inicio = int(round(time.time() * 1000))
	i=0 # hasta 320
	for j in range(alto):
		for k in range(1, ancho*2, 2):
			if memPix[j][k]=="1":
				pix[i,j]=(255,255,255)
			else:
				pix[i,j]=(0,0,0)
			i+=1
		i=0
	img=ImageOps.mirror(img) # verificar si es necesario
	img.save(getRuta(filename)+"_umbralizado.bmp")
	fin = int(round(time.time() * 1000))
	cronometro=fin-inicio
	print(">> Conversion completa, tiempo transcurrido %d ms" % cronometro)
except:
	print(">> La imagen no pudo ser cargada correctamente")