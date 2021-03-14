import csv
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

def mega_sena(game):
    result = ''
    match = ''
    with open('mega.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            result = set(row[2:-2])
            match = game.intersection(result)
            if len(match) == 4:
                print(f'Voce poderia ter ganho na quadra em {row[1]} {row[2:-2]}')
            if len(match) == 5:
                print(f'Voce poderia ter ganho na quina em {row[1]} {row[2:-2]}')
            if len(match) == 6:
                print(f'Voce poderia ter ganho na sena em {row[1]} {row[2:-2]}')

def lotto(game):
    
    result = dict()
    match = ''
    with open('lotto.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            result['balls'] = set(row[2:-2])
            result['powerball'] = row[-1]
            match =  game.get('balls').intersection(result.get('balls'))
            if len(match) == 6 and result.get('powerball') != game.get('powerball'):
                print(f'Voce poderia ter ganho na lotto em {row[1]} {row[2:-2]}')
            if len(match) == 6 and result.get('powerball') == game.get('powerball'):
                print(f'Voce poderia ter ganho na powerball em {row[1]} {row[2:-2]} {row[-1]}')
            if len(match) == 5:
                print(f'Voce acertou 5 dezenas em {row[1]} {row[2:-2]}')
            if len(match) == 4:
                print(f'Voce acertou 4 dezenas em {row[1]} {row[2:-2]}')
            
@app.route('/', methods=['GET', 'POST'])
def home():
    lista = []
    results = dict()
    if request.method == 'POST':
        dez1 = request.form.get('dez_01')
        dez2 = request.form.get('dez_02')
        dez3 = request.form.get('dez_03')
        dez4 = request.form.get('dez_04')
        dez5 = request.form.get('dez_05')
        dez6 = request.form.get('dez_06')
        mygame = {dez1, dez2, dez3, dez4, dez5, dez6}
        mygame = set([item.replace("0","") if int(item)<=10 else item for item in mygame ])
        
        result = ''
        match = ''
        
        with open('mega.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                
                result = set(row[2:-2])
                match = mygame.intersection(result)
                if len(match) == 4:
                    results = {'date':row[1], 'matches': len(match), 'escolhidos':match, 'result': result,'ganhadores':row[-2], 'quantia':row[-1]}
                    lista.append(results)
                    
                elif len(match) == 5:
                    results = {'date':row[1], 'matches': len(match), 'escolhidos':match, 'result': result,'ganhadores':row[-2], 'quantia':row[-1]}
                    lista.append(results)
                   
                elif len(match) == 6:
                    results = {'date':row[1], 'matches': len(match), 'escolhidos':match, 'result': result,'ganhadores':row[-2], 'quantia':row[-1]}
                    lista.append(results)
                
    return render_template('index.html', res = lista)

if __name__ == '__main__':
    app.run(debug=True)


        
