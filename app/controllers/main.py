from app.controllers.cod import cpf,cnpj
from flask import render_template, request
from app import app
from app.models.forms import Campos

@app.route('/', methods=["GET","POST"])
def index():
    form = Campos()
    if form.validate_on_submit():
        op = str(form.es.data)
        if (len(op) == 11):
            result = cpf.valida_cpf(op)
            valido = 1 if result else 0
            return render_template('index.html',form=form, valido=valido, dado=op),200
        elif (len(op) > 11):
            result = cnpj.valida_cnpj(op)
            valido = 1 if result else 0
            return render_template('index.html',form=form, valido=valido, dado=op),200
        else:
            if request.form["op"] == 'cpf':
                return render_template('index.html',form=form, valido=cpf.valida_cpf(cpf.gerar_cpf()),dado=cpf.gerar_cpf()),200
            else:
                dado = cnpj.gerar_cnpj()
                return render_template('index.html',form=form, valido=cnpj.valida_cnpj(cnpj.gerar_cnpj()), dado=dado),200
    
    return render_template('index.html',form=form),200