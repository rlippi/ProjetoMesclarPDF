# Projeto - vamos mesclar os arquivos PDF.pdf, Arquivo.pdf e Ultimo Arquivo.pdf

# Biblioteca que permite manipular arquivos em PDF --> instalar
import PyPDF2
# Biblioteca os --> manipular arquivos do computador, ler arquivos de uma pasta, etc.Z
import os


# criar o mesclador
merger = PyPDF2.PdfMerger()

#listar os arquivos da pasta "arquivos"
lista_arquivos = os.listdir("arquivos")
#colocar os arquivos em ordem alfabética
lista_arquivos.sort()

#print(lista_arquivos)

#colocamos o for para varrer a lista arquivos e se a extensão for pdf 
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write(f"arquivos/Pdf_final_criado_com_sucesso.pdf")