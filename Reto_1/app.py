from flask import Flask
from model.CovidDataFrame import CovidDataFrame

app = Flask(__name__)

@app.route('/')
def hello_world():
    covid_df = CovidDataFrame()
    return covid_df.getDataFrame().to_html()

if __name__ == '__main__':
    app.run()


