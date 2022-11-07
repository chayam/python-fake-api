
from Util import Util
class FakeApi():
    baseUrl = "https://jsonplaceholder.typicode.com"
    

    def __init__(self,baseUrl:str=baseUrl):
        self.baseUrl = baseUrl
        pass
    
    def getTodos(self,method:str='get'):
        
        path = '/todos'
        url = self.baseUrl+path
        print('aqui')
        print(Util.getIntervalTime(type='minutes',time=1))
        data = Util.genericCall(self,url=url,method=method,verify=True)   
        if (not data['error']):
            return data 
        return None
    
    
