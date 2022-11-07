import logging,os

class Logging:
    def __init__(self):
        pass
    
    def requestedApiLog(status_code:int,content):
        from Util import Util
        
        filename='apilog.log'
        dataAtual = Util.currentDateTime()
        logging.basicConfig(filename=filename, level=logging.INFO)
        if (status_code == 200):
            msg=f"Resquest OK, requisicao efetuada com sucesso! {dataAtual}"
            logging.info(f"\n  {msg} \n {content} \n")
        elif (status_code == 400):
            msg=f"Bad request, verifique a requisicao! {dataAtual}"
            logging.warning("\n  {msg} \n {content} \n", exc_info=os.environ['loggingExecInfo'])
        elif (status_code == 404):
            msg = f"request not found, verifique a requisicao! {dataAtual}"
            logging.warning(f"\n  {msg} \n {content} \n", exc_info=os.environ['loggingExecInfo'])
        elif (status_code == 500):
            msg = f"internal server error, erro no servidor! {dataAtual}"
            logging.error(f"\n  {msg} \n {content} \n", exc_info=os.environ['loggingExecInfo'])
        else:
            msg = f"Um erro ocorreu inesperado, verifique o log! {dataAtual}"
            logging.error(f"\n  {msg} \n {content} \n",content, exc_info=os.environ['loggingExecInfo'])
        return None