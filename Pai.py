from os.path import isdir, isfile, join
from os import listdir, system
from time import sleep
from PIL import Image, ImageTk
from tkinter import Canvas, Tk
from multiprocessing import Process


def cadastrarPasta(invalid = False):
	system("cls")
	if invalid: print("Diretório inválido!")
	print("Insira o diretório COMPLETO para monitorar:")
	print(r"Ex: C:\Users\Joao\Fotos")
	pasta = input()
	if not isdir(pasta): 
		cadastrarPasta(invalid = True)
	else:
		with open(".settings.txt", "w") as txt:
			txt.write(pasta)
		print("Configuração Salva")
		system("cls")
		
def getFolder():
	try:
		with open(".settings.txt", "r") as txt:
			try: return txt.readlines()[0]
			except IndexError: cadastrarPasta()
	except FileNotFoundError:
		cadastrarPasta()
		return getFolder()


class Overwatch():

	def __init__(self):
		self.folder = getFolder()
		self.img = None
		self.imagens = []
		self.thread = Process(target=self.showImg)
		self.start()


	def update(self):
		self.imagensLastLoop = self.imagens
		self.imagens = [img for img in listdir(self.folder) if any([img.endswith("png"), img.endswith("jpg"), img.endswith("jpeg")])]
		if len(self.imagens) == 0:
			print("Nenhuma imagem encontrada no diretório, favor adicionar ao menos uma imagem e apertar ENTER para continuar.")
			input()
			self.update()

	def start(self):
		while True:
			self.update()
			error = True
			if not self.thread.is_alive():
				print("Selecione uma imagem para abrir")
				for imgName,count in zip(self.imagens, range(len(self.imagens))):
					print(f"{count} - {imgName}")
				imgName = self.imagens[int(input())]
				while error:
					try:
						self.img = Image.open(join(self.folder, imgName))
						error = False
					except PermissionError: pass
				self.show()
			elif len(self.imagens) > len(self.imagensLastLoop):
				self.hide()
				imgName = [img for img in self.imagens if img not in self.imagensLastLoop][0]
				while error:
					try:
						self.img = Image.open(join(self.folder, imgName))
						error = False
					except PermissionError: pass
				self.show()


	def hide(self):
		self.thread.terminate()


	def show(self):
		print("Showing Thread")
		del self.thread
		self.thread = Process(target=self.showImg)
		self.thread.start()
		print("Status: {}".format(self.thread.is_alive()))


	def showImg(self):
		print("Showing Img")
		root = Tk()
		w, h = root.winfo_screenwidth(), root.winfo_screenheight()
		root.overrideredirect(1)
		root.geometry("%dx%d+0+0" % (w, h))
		root.focus_set()    
		root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
		canvas = Canvas(root,width=w,height=h)
		canvas.pack()
		canvas.configure(background='black')
		imgWidth, imgHeight = self.img.size
		if imgWidth > w or imgHeight > h:
			ratio = min(w/imgWidth, h/imgHeight)
			imgWidth = int(imgWidth*ratio)
			imgHeight = int(imgHeight*ratio)
			self.img = self.img.resize((imgWidth,imgHeight), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(self.img)
		imagesprite = canvas.create_image(w/2,h/2,image=image)
		root.mainloop()


if __name__ == "__main__":
	Overwatch()
