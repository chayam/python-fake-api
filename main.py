
# [START gae_python37_app]
from flask import Flask
from services.FakeApi import FakeApi
from models.FakeExample import FakeExample
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():   
    return 'Projeto funcionando, parabens!!!'

@app.route('/all')
def all():
    fa = FakeApi()
    response = fa.getTodos()
       
    if response is not None:
        model = FakeExample()
        dataframe = pd.DataFrame(data=response['body'])
        dataframe = model.transformData(dataframe)
        return dataframe.to_html()   
    return 'Não há dados'

@app.route('/filter',defaults={'filter':'','typefilter':'like'})
@app.route('/filter/<filter>/<typefilter>')
def allfilter(filter:str,typefilter:str):
    fa = FakeApi()
    response = fa.getTodos()
    
    if response is not None:
        model = FakeExample()
        dataframe = pd.DataFrame(data=response['body'])
        dataframe = model.transformData(dataframe)       
        # dataframe =  dataframe.loc[dataframe['title'].str.contains(filter, case=False)] # igual ao like %string%
        # dataframe =  dataframe.loc[dataframe['title'].str.match(filter, case=False)] # igual ao like string%
        dataframe = model.filterExample(dataframe,filter,typefilter)
        dataframe = dataframe.reset_index(drop=True)
        return dataframe.to_html()   
    return 'Não há dados'

@app.route('/completed')
def completed():
    fa = FakeApi()
    response = fa.getTodos()
       
    if response is not None:
        dataframe = pd.DataFrame(data=response['body'])
        dataframe=dataframe.groupby("completed").size().reset_index(name='qtd')
        return dataframe.to_html()   
    return 'Não há dados'

    
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8082, debug=True) 
# [END gae_python37_app]