# Organizador
# Versão 0.0.1
# Autor: Raul T. Sibemberg
# Data: 04/09/2022
# Descrição: Programa para guardar arquivos em pastas de acordo com 
# suas extensões. 



import os
import shutil
   



# Defina abaixo o diretório que deseja organizar (entre as '')

path = '\\caminho\\para\\a\\pasta'


# Cria lista de arquivos no diretório

arquivos = os.listdir()
   
# Escaneia extensões no diretório

for arquivo in arquivos:
    name, ext = os.path.splitext(arquivo)
  
# Guarda as extensões

    ext = ext[1:]


# Força iterações

    if ext == '':
        continue

# Move arquivos para diretório da extensão se já existir
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+arquivo, path+'/'+ext+'/'+arquivo)
  
# Cria diretórios para as extensões caso não existam
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+arquivo, path+'/'+ext+'/'+arquivo)