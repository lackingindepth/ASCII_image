from PIL import Image # Biblioteca para manipulação de imagens
from tkinter import Tk # Biblioteca para interface gráfica
from tkinter.filedialog import askopenfilename # Função para abrir diálogo de seleção de arquivo

Tk().withdraw() # Oculta a janela principal do Tkinter

# Abre o diálogo para selecionar um arquivo de imagem
caminho_do_arquivo = askopenfilename(title="Selecione uma imagem:", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")])


# Verifica se um arquivo foi selecionado
if caminho_do_arquivo:

    imagem = Image.open(caminho_do_arquivo) #carrega a imagem selecionada

    # Redimensionar a imagem para largura fixa mantendo a proporção
    largura, altura = imagem.size
    nova_largura = 100
    proporcao = nova_largura / float(largura) # Calcula a proporção de redimensionamento

    nova_altura = int(float(altura) * proporcao * 0.55) # Ajusta a altura para manter a proporção visual

    imagem_redimensionada = imagem.resize((nova_largura, nova_altura))# Redimensiona a imagem

    # Converte a imagem para escala de cinza
    imagem_cinza = imagem_redimensionada.convert("L")

    # Mapeia os níveis de cinza para caracteres ASCII
    caracteres_ascii = "@%#*+=-:. "

    pixels = imagem_cinza.getdata() 

    ascii_str = "" # String para armazenar a representação ASCII

    # Constrói a string ASCII
    for i in range(len(pixels)): # Itera sobre cada pixel

        #Obtem o nível de cinza do pixel
        nivel_de_cinza = pixels[i] 
        # Mapeia o nível de cinza para um caractere ASCII
        indice_caractere = nivel_de_cinza * (len(caracteres_ascii) - 1) // 255 
        # Adiciona o caractere correspondente à string ASCII
        ascii_str += caracteres_ascii[indice_caractere] 
        # Adiciona uma nova linha após atingir a largura definida
        if (i + 1) % nova_largura == 0: 
            ascii_str += "\n"

    # Salva a string ASCII em um arquivo de texto
    with open("imagem_ascii.txt", "w") as arquivo_txt:
        arquivo_txt.write(ascii_str)

    print("Imagem ASCII salva em 'imagem_ascii.txt'")

