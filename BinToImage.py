from tkinter.filedialog import askopenfilename
from PIL import Image
import time

"""
	Convierte de decimal a binario
"""
def binToDecimal(bin):
	return int(bin,2)

"""
	Carga una imagen binaria de una ruta
"""
def openImagen(ruta):
	temp=[]
	f=open(ruta, "r")
	fl =f.readlines()
	for x in fl:
		temp.append(x[:len(x)-1])
	return temp

"""
	Convierte una linea binaria a RGB /tupla
"""
def getRGB(dato):
	temp=[]
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	#return tuple(temp[::-1])
	return tuple([temp[2],temp[2],temp[2]])

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

try:
	ancho,alto=(320, 240);
	img = Image.new('RGB', (ancho,alto), color = 'red') # imagen base
	pix=img.load()
	filename = askopenfilename()
	imagen1D=openImagen(filename)
	inicio = int(round(time.time() * 1000))
	i=0 # hasta 320
	j=0 # hasta 240

	for k in range(ancho*alto):
		if i==(ancho-1):
			pix[i,j]=getRGB(imagen1D[k])
			j+=1
			i=0
		else:
			pix[i,j]=getRGB(imagen1D[k])
			i+=1

	img.save(getRuta(filename)+"_new.bmp")
	fin = int(round(time.time() * 1000))
	cronometro=fin-inicio
	print(">> Conversion completa, tiempo transcurrido %d ms" % cronometro)
	
except:
	print(">> La imagen no pudo ser cargada correctamente")