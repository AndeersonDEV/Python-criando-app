import pandas as pd
def trabalhar_arquivo():
    tabela = pd.read_excel('base/servicenow.xlsx')
    tabela.drop(tabela.columns[[1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]], axis= 1 , inplace= True )

    tabela.loc[tabela['Estado'] == 'Fechado', 'Estado'] = 'Fim da analise'

    tabela.to_json('base/painel2.json')

def main():
    trabalhar_arquivo()
    

if __name__ == '__main__':
    main()