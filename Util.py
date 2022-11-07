from datetime import datetime,timedelta
from calendar import month,monthrange
from dateutil.relativedelta import relativedelta
from urllib.parse import urlparse
import unicodedata,re,time,pytz,requests,json,base64,pandas as pd,numpy as np

import concurrent.futures
from dotenv import load_dotenv
import time, uuid,os,pprint as prt

class Util:

    def __init__(self):
        pass
    
    def generanteId():
        return Util.baseEncodeString(Util.convertDatetimeToString(Util.currentDateTime(),'%Y-%m-%d %H:%M:%S.%f'))
    
    def generanteUid():
        return uuid.uuid1()
    
    def geraTimestamp():
        return time.strftime("%Y%m%d%H%M%S")

    def timestampNow():
        
        agora = datetime.now()

        dataAlterada = agora.strftime('%Y-%m-%d %H:%M:00')
        x=datetime.strptime(dataAlterada, '%Y-%m-%d %H:%M:00')

        return int(x.timestamp())

    def timestampLast24h():

        agora = (datetime.now()-timedelta(days=1))

        dataAlterada = agora.strftime('%Y-%m-%d %H:%M:00')
        x=datetime.strptime(dataAlterada, '%Y-%m-%d %H:%M:00')
        
        return int(x.timestamp())

    def diffBetweenDatesInSeries(endDateSeries:pd.Series=None,beginDateSeries:pd.Series=None,typeResult:str='s'):
        diff = (endDateSeries - beginDateSeries)/np.timedelta64(1,typeResult)
        return diff

    def convertStringtoDatetime(stringDate,mask='%Y-%m-%d %H:%M:%S'):
        
        data = datetime.strptime(stringDate, mask) 
        
        return data

    def convertDatetimeToString(paramDatetime:datetime,mask='%Y-%m-%d %H:%M:%S'):
        
        formatDatetime = paramDatetime.strftime(mask)
        
        return formatDatetime

    def currentDateTime():
        PYTZ =pytz.timezone(os.environ["TIMEZONE"])
        agora = datetime.now(PYTZ) 
        
        return agora
    
    def convertTimestampToSecond(paramDatetime:datetime):        
        medida = (paramDatetime - datetime(1970,1,1)).total_seconds()
        return medida

    def convertMilisecondsToTimestamp(milisegundos):
        return datetime.fromtimestamp(milisegundos/1000.0)
        
    def convertJsonToString(vJson:dict):
        result = json.dumps(vJson)
        return result
    
    def checkExtension(caminho,extension,enconding,delimitador):
        if(extension in ['.xls','.xlsx']):
            return pd.read_excel(caminho)
        elif(extension in ['.csv']):
            # return pd.read_csv(caminho,encoding="ISO 8859-1", delimiter=',')
            return pd.read_csv(caminho,encoding=enconding, delimiter=delimitador)
    
    def normalizandoString(string):
        string = str(string)
        string = string.lstrip()
        string = string.replace(' ','_').lower()
        string = re.sub('[`\.*\`":()!@]', '', string)
        string = ''.join(ch for ch in unicodedata.normalize('NFKD', string) if not unicodedata.combining(ch))
        
        return string
        
    def separaString(string:str,separador:str,indice:int=0):
        try:
            v = string.split(separador)[indice]
        except Exception as e:
            v = string
        return v
    
    def listaValoresEmlinha(dataframe,nameColumn):
        numbers = "','".join([str(x) for x in dataframe[nameColumn].tolist()])        
        return '\''+numbers+'\''
    
    def baseEncodeString(value):
        value = str(value)
        message_bytes = value.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def baseDecodeString(value):
        value = str(value)
        base64_message = base64.b64decode(value)
        # base64_message = base64_bytes.decode('ascii')
        return base64_message

    def getIntervalTime(type,time):
        time = int(time)
        dt_fim = datetime.now() 
        dt_ontem = (datetime.now() - timedelta(days= 1) )

        if type == 'seconds':
            dt_inicio =  datetime.now() - timedelta(seconds= time)
            dt_inicio = dt_inicio.strftime('%Y-%m-%d %H:%M:%S')
            dt_fim = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        elif type == 'minutes':
            dt_inicio = datetime.now() - timedelta(minutes= time)
            dt_inicio = dt_inicio.strftime('%Y-%m-%d %H:%M:00')
            dt_fim = datetime.now().strftime('%Y-%m-%d %H:%M:59') 
        elif type == 'hours':
            dt_inicio = datetime.now() - timedelta(hours= time)
            dt_inicio = dt_inicio.strftime('%Y-%m-%d %H:00:00')
            dt_fim = datetime.now().strftime('%Y-%m-%d %H:59:59')  
        elif type == 'days':
            dt_inicio = datetime.now() - timedelta(days= time)
            dt_inicio = dt_inicio.strftime('%Y-%m-%d 00:00:00')
            dt_fim = dt_ontem.strftime('%Y-%m-%d 23:59:59')
        elif type == 'current':
            dt_inicio = datetime.now().strftime('%Y-%m-%d 00:00:00')
            dt_fim = datetime.now().strftime('%Y-%m-%d 23:59:59')
        elif type == 'weeks':
            dt_inicio = datetime.now() - timedelta(weeks= time)
            dt_inicio = dt_inicio.strftime('%Y-%m-%d 00:00:00')
            dt_fim = dt_ontem.strftime('%Y-%m-%d 23:59:59')
        elif type == 'months':
            dt_inicio = datetime.now() - relativedelta(months=time)
            dt_inicio = dt_inicio.strftime('%Y-%m-01 00:00:00')
            last_day = monthrange(int(datetime.now().strftime('%Y')),int(((datetime.now() - relativedelta(months=time))).strftime('%m')))[1]
            last_month = (datetime.now() - relativedelta(months=time)).strftime('%m')
            last_year = (datetime.now() - relativedelta(months=time)).strftime('%Y')
            dt_fim = dt_ontem.strftime(last_year+'-'+last_month+'-'+str(last_day)+' 23:59:59')
        else:
            dt_inicio = datetime.now()
            return 'Invalido'
        
        return [dt_inicio,dt_fim]
        
    def genericCall(self,url,body=None,verify=False,method='get',auth=None,headers=None):
        try:
            url = url
            if (method == 'post'):
                req = requests.post(url=url,data=body,headers=headers,verify=verify,auth=auth)
            else:
                req = requests.get(url,data=body,headers=headers,verify=verify,auth=auth)
            
            # print('aqui')
            # print(url)
            # print(method)
            # print(headers)
            # print(body)
            # print(req.status_code)
            # print(req.content)
            responseInfo = {
                            "url":url,
                            "method":method,
                            "headers":headers,
                            # "body":req.content,
                            "status_code":req.status_code
                           } 
            data = {"body":{},"error":True}
            status_code = int(req.status_code)
            
            # efetuando log das requisições
            # lg.requestedApiLog(status_code,responseInfo)
            
            prt.pprint(responseInfo)
            if (status_code == 200):
                data = {"body":json.loads(req.content),"error":False}
            elif (status_code == 400):
                msg="Bad request, verifique a requisicao"
                raise Exception(status_code, msg)
            elif (status_code == 404):
                msg="request not found, verifique a requisicao"
                raise Exception(status_code, msg)
            elif (status_code == 500):
                msg="internal server error, erro no servidor"
                raise Exception(status_code, msg)
            else:
                raise Exception(status_code, "Um erro ocorreu inesperado, verifique o log")
        except Exception as e:
            data = {"body":e,"error":True}
            # print(e)
        return data
    
    def uptadeJson(origem:dict,newValue:dict):
        if len(newValue) > 0:
            origem.update(newValue)
        return origem
    
    def uptadeValueJson(origem:dict,key:str,value):
        origem[key] = value
        return origem
    
    def processamentoCustom(function:any,args:any):
        start = time.perf_counter()
        dfResult = pd.DataFrame()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(function,args)
            for result in results:
                # print(result)
                dfResult = dfResult.append(json.loads(result),ignore_index=True)
        finish = time.perf_counter()
        print(f'Finished in {round(finish-start,2)} second(s)')
        return dfResult