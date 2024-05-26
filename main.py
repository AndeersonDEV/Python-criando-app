import shutil
import os 
from os import chdir, getcwd, listdir
import edicao as edicao
def identificar_nome_do_arquivo():
    caminho = "C:/Users/Andee/OneDrive/Área de Trabalho/Download/"
    pastas_e_arquivos = os.listdir(caminho)

    for elemento in pastas_e_arquivos:
        # if(os.path.isfile(caminho + elemento)):
        elemento
            

    os.rename(f'C:/Users/Andee/OneDrive/Área de Trabalho/Download/{elemento}', 'C:/Users/Andee/OneDrive/Área de Trabalho/Download/servicenow.xlsx')
    
    shutil.move('C:/Users/Andee/OneDrive/Área de Trabalho/Download/servicenow.xlsx','C:/Users/Andee/OneDrive/Área de Trabalho/Nova pasta (6)/base')
    


def apagar_base():
    
    os.remove('C:/Users/Andee/OneDrive/Área de Trabalho/Nova pasta (6)/base/servicenow.xlsx')

def trocar_de_pasta(nome):
    os.rename(f'C:/Users/Andee/OneDrive/Área de Trabalho/Download/{nome}', 'C:/Users/Andee/OneDrive/Área de Trabalho/Download/servicenow.xlsx')
    
    shutil.move('C:/Users/Andee/OneDrive/Área de Trabalho/Download/servicenow.xlsx','C:/Users/Andee/OneDrive/Área de Trabalho/Nova pasta (6)/base')


def main():
    apagar_base()
    identificar_nome_do_arquivo()
    edicao.trabalhar_arquivo()

if __name__ == '__main__':
    main()
