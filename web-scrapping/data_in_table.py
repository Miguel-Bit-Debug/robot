from bs4 import BeautifulSoup

file = open('./arquivos/data_in_table.html', mode='r', encoding='utf-8')
soup = BeautifulSoup(file, 'html.parser')

table = soup.find(id='main_table')
table_rows = table.find_all('tr')

dados_alunos = []

for linha in table_rows:
    colunas = linha.find_all("td")

    if(len(colunas) > 0):
        codigo_aluno = colunas[0].text
        nome_aluno = colunas[1].text
        nota_aluno = colunas[2].text
        
        dict_aluno = {
            "codigo": codigo_aluno,
            "nome": nome_aluno,
            "nota": nota_aluno
        }

        dados_alunos.append(dict_aluno)
        print(f"{codigo_aluno} - {nome_aluno} - {nota_aluno}")

print(dados_alunos)