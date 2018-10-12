from tkinter.filedialog import askopenfilename
from PIL import Image

def binToDecimal(bin):
	return int(bin,2)

def openImagen(ruta):
	temp=[]
	f=open(ruta, "r")
	fl =f.readlines()
	for x in fl:
		temp.append(x[:len(x)-1])
	return temp

def getRGB(dato):
	temp=[]
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	dato=dato[8:]
	temp.append(binToDecimal(dato[:8]))
	return tuple(temp[::-1])

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

ancho,alto=(320, 240);
img = Image.new('RGB', (ancho,alto), color = 'red') # imagen base
pix=img.load()
filename = askopenfilename()
imagen1D=openImagen(filename)

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

img.save(getRuta(filename)+".bmp")
