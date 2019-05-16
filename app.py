from flask import Flask, jsonify, request, render_template
import re
from formulas import formulas

app = Flask(__name__)

@app.route('/')
def static_page():
    return render_template('index.html')

@app.route('/trimf/<string:lista>')
def Func_trimf(lista):
    
    trata_lista = lista.split(',')
    trata_lista = [float(i) for i in trata_lista]

    if len(trata_lista) != 4:
        return "Você deve passar 4 elementos. Ex: /trimf/5,4,3,7"
    else:
        fz = formulas()
        result = fz.trimf(*trata_lista)
        return jsonify(result=result)

@app.route('/tramf/<string:lista>')
def Func_tramf(lista):
    
    trata_lista = lista.split(',')
    trata_lista = [float(i) for i in trata_lista]

    if len(trata_lista) != 5:
        return "Você deve passar 5 elementos. Ex: /tramf/7,6,5,8,5"
    else:
        fz = formulas()
        result = fz.tramf(*trata_lista)
        return jsonify(result=result)



if __name__ == '__main__':
    app.run(debug=True)