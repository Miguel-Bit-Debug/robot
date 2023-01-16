from bs4 import BeautifulSoup

file = open('./arquivos/data_in_table_2.html', mode='r', encoding='utf-8')
soup = BeautifulSoup(file, 'html.parser')

table = soup.find_all('table')[1]
table_rows = table.find_all('tr')

dados_cursos = []

for linha in table_rows:
    colunas = linha.find_all("td")

    if(len(colunas) > 0):
        curso = colunas[0]
        interesse = colunas[1]

        curso_dict = {
            "curso": curso,
            "interesse": interesse
        }

        dados_cursos.append(curso_dict)


print(dados_cursos)