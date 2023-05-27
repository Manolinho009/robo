from flask import Flask, request
import json
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/salvar_html', methods=['POST'])
def write_html():
    # Lê o HTML enviado no corpo da requisição
    html = request.data.decode('utf-8')
    j = json.loads(html)

    # Escreve o HTML em um arquivo
    with open('pagina.html', 'w', encoding='utf-8') as f:
        f.write(j['html'])

    with open('pagina.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        # extraindo as tags <article> e <p>
        prova = soup.find('div',{'class':"question"})
        final = ''

        questoes = prova.find_all('div',attrs={"data-ordem":True})
        
        for qr in questoes:
            str_quest = ''
            perguntas = qr.find_all(class_="question-text")
            for p in perguntas:
                str_quest += p.text
            resposta = ''
            for tr in qr.find_all('tr',{'class':'question-choice'}):
                resposta  += str(tr)
                resposta  += '<br>' 
            final += str_quest+'<br>'+resposta+'<br><br>'
        

        with open("resp.html", "w", encoding='utf-8') as f:
            f.write(final)
    # Retorna uma resposta para o cliente
    return 'HTML gravado com sucesso!'


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='localhost')
