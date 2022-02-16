from flask import Flask
from flask import render_template, request
from model.CovidDataFrame import CovidDataFrame

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    covid_df = CovidDataFrame()

    if request.method == 'GET':
        return render_template('index.html', data=covid_df.getDataFrame().to_html(),
                               paises=covid_df.getListaPaises(),
                               departamentos=covid_df.getListaDepartamentos(),
                               dataEdad=None,
                               dataGenero=None,
                               dataDepartamentos=None,
                               dataDepartamentoEdad=None,
                               dataPaises=None)

    try:
        if request.form["consultarEdad"] != None:
            edad = request.form["edad"]
            if edad == "":
                return render_template('index.html', data=covid_df.getDataFrame().to_html(),
                                       dataEdad=None,
                                       dataGenero=None, dataDepartamentos=None,
                                       paises=covid_df.getListaPaises(),
                                       departamentos=covid_df.getListaDepartamentos(),
                                       dataDepartamentoEdad=None,
                                       dataPaises=None
                                       )
            else:
                edad = int(edad)
                return render_template('index.html',
                                       data=covid_df.getDataFrame().to_html(),
                                       dataEdad=covid_df.getDatosPorEdad(edad).to_html(),
                                       dataGenero=None,
                                       dataDepartamentos=None,
                                       paises=covid_df.getListaPaises(),
                                       departamentos=covid_df.getListaDepartamentos(),
                                       dataDepartamentoEdad=None,
                                       dataPaises=None
                                       )
    except:
        "No se consulto edad"

    try:
        if request.form["consultarGenero"] != None:
            genero = request.form["genero"]
            return render_template('index.html',
                                   data=covid_df.getDataFrame().to_html(),
                                   dataGenero=covid_df.getDatosPorGenero(genero).to_html(),
                                   dataEdad=None, dataDepartamentos=None,
                                   paises=covid_df.getListaPaises(),
                                   departamentos=covid_df.getListaDepartamentos(),
                                   dataDepartamentoEdad=None,
                                   dataPaises=None)
    except:
        print("No se consulto genero")

    try:
        if request.form["consultarDepartamento"] != None:
            departamento = request.form["departamento"]
            return render_template('index.html',
                                   data=covid_df.getDataFrame().to_html(),
                                   dataGenero=None,
                                   dataEdad=None,
                                   paises=covid_df.getListaPaises(),
                                   departamentos=covid_df.getListaDepartamentos(),
                                   dataDepartamentos=covid_df.getDatosPorDepartamento(departamento).to_html(),
                                   dataDepartamentoEdad=None,
                                   dataPaises=None)

    except:
        print("no se consulto departamento")

    try:
        if request.form["consultarDepartamentoyEdad"] != None:
            edad = request.form["edad"]
            departamento = request.form["departamento"]
            if edad == "":
                return render_template('index.html',
                                       data=covid_df.getDataFrame().to_html(),
                                       dataEdad=None,
                                       dataDepartamentoEdad=None, dataGenero=None,
                                       dataDepartamentos=None,
                                       paises=covid_df.getListaPaises(),
                                       departamentos=covid_df.getListaDepartamentos(),
                                       dataPaises=None)
            else:
                edad = int(edad)
                return render_template('index.html', data=covid_df.getDataFrame().to_html(),
                                       dataDepartamentoEdad=covid_df.getDatosPorDepartamentoyEdad(departamento,
                                                                                                  edad).to_html(),
                                       dataEdad=None, dataGenero=None,
                                       dataDepartamentos=None,
                                       paises=covid_df.getListaPaises(),
                                       departamentos=covid_df.getListaDepartamentos(),
                                       dataPaises=None
                                       )
    except:
        "No se consulto edad"

    try:
        if request.form["consultarPais"] != None:
            pais = request.form["pais"]
            return render_template('index.html',
                                   data=covid_df.getDataFrame().to_html(),
                                   dataGenero=None,
                                   dataEdad=None,
                                   paises=covid_df.getListaPaises(),
                                   departamentos=covid_df.getListaDepartamentos(),
                                   dataDepartamentos=None,
                                   dataDepartamentoEdad=None,
                                   dataPaises=covid_df.getDatosPorPaisOrigen(pais).to_html())

    except:
        print("no se consulto pais")


@app.route('/integrantes')
def getIntegrantes():
    integrantes = ["Jose Alejandro Cortazar Lopez", "Alvaro Alejandro Zarabanda Gutierrez"]
    return render_template('integrantes.html', integrantes=integrantes)


if __name__ == '__main__':
    app.run(debug=True)
