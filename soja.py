from flask import Flask, request, render_template,redirect,url_for
import pandas as pd



app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def submitForm():
  valu=''
  values=''
  producto = ''
  indicador =''
  label_date=''
  percent=''
  lista=''


  url_soja='https://www.cepea.esalq.usp.br/br/indicador/soja.aspx'

  url_trigo='https://www.cepea.esalq.usp.br/br/indicador/trigo.aspx'


  url_milho='https://www.cepea.esalq.usp.br/br/indicador/milho.aspx'

  url_boi='https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx'

  url_bezerro='https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx'

  url_algodao='https://www.cepea.esalq.usp.br/br/indicador/algodao.aspx'

  if request.method == 'POST':
    producto = request.form['select1']
    indicador = request.form['select2']
   
 

    if producto=='soja':
        url=url_soja
        
        tabla=pd.read_html(url)

        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
    elif producto=='trigo':
        url=url_trigo
        
        tabla=pd.read_html(url)
        
        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
    elif producto=='milho':
        url=url_milho
        
        tabla=pd.read_html(url)
        
        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
    elif producto=='boi':
        url=url_boi
        tabla=pd.read_html(url)
        
        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
    elif producto=='bezerro':
        url=url_bezerro
        tabla=pd.read_html(url)
        
        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
    elif producto=='algodao':
        url=url_algodao
        tabla=pd.read_html(url)
        tablo=tabla[0]
        tablo.columns = ['date', 'reales', 'dia', 'mes', 'dolar']
        
     
    label_date=  tablo['date'].values.tolist()
     
    dates=[]
    for i in label_date:
        corte=i.split('/')
        d=corte[0]+'/'+corte[1]
        dates.append(d)

    if indicador=='VALOR R$':
      values=  tablo['reales'].values.tolist()
    elif indicador=='VAR./DIA':
      values=  tablo['reales'].values.tolist()
      percent =tablo['dia'].values.tolist()
    elif indicador=='VAR./MES':
      values=  tablo['reales'].values.tolist()
      percent=tablo['mes'].values.tolist()
    elif indicador=='VALOR US$':
      values= tablo['dolar'].values.tolist()
    
    valu=[]
    for v in values:
        v=str(v)
        vv=v[:3]+','+v[3:]
        valu.append(vv)

  
    if indicador=='VAR./DIA':
        listas=zip(dates, percent)
        listas=list(listas)
        lista=listas[:5]
    elif indicador=='VAR./MES':
        listas=zip(dates, percent)
        listas=list(listas)
        lista=listas[:5]
    elif indicador=='VALOR US$':
        listas=zip(dates, valu)
        listas=list(listas)
        lista=listas[:5]
    elif indicador=='VALOR R$':
        listas=zip(dates, valu)
        listas=list(listas)
        lista=listas[:5]

  return render_template('soja2.html',values=values,labels=label_date,lista=lista,percent=percent)


if __name__ == '__main__':
  app.run()
