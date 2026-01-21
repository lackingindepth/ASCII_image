## Script python que converte pixels em escalas de cinza e os transforma em ASCII(@%#*+=-:. )

## Tecnologias Usadas

- **Python 3.x**
- **Pillow (PIL)** - Manipulação de imagens
- **tkinter** - Interface de seleção de arquivos

## Pré-requisitos

### Ubuntu/Debian
```bash
sudo apt install python3-tk
```

## Outras distribuições Linux
Consulte o gerenciador de pacotes da sua distro para instalar `python3-tk`

##  Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/image-pixel-processor.git
cd image-pixel-processor
```

2. Crie um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install pillow numpy
```

## Como Usar

Execute o script:
```bash
python ascii.py
```

 Uma janela de seleção de arquivos será aberta. Escolha a imagem que deseja processar.

## Funcionalidades

- Seleção de imagens via interface gráfica
- Acesso individual a cada pixel
- Modificação de valores RGB
- Suporte para múltiplos formatos (PNG, JPG, GIF, BMP)


## Aprendizados

- Manipulação de pixels usando Pillow
- Diferença entre acesso individual vs operações em lote com NumPy
- Integração de tkinter para seleção de arquivos
- Estruturação de ambientes virtuais em Python






---
