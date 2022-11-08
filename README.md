# python-fake-api
Projeto que simula a busca de dados em uma API, e utiliza o pandas para manipulação dos dados. Projeto também conta com um módulo de Log, para facilitar possível erros e mensagens.

# Versão do python e Bibliotecas utilizadas.

<b>Python</b>: <code>3.7.0</code><br/>
<b>Libs</b>: <code>Flask,requests,pandas,python-dotenv</code>


# Download do python
Intale o <a href="https://www.python.org/downloads/" target="_blank"> python</a> de acordo com a versão do seu PC.

# Instale o github
Intale o <a href="https://git-scm.com/downloads" target="_blank">github</a> de acordo com o seu SO(Sistema Operacional).
# Faça o clone do projeto
Com o git instalado e configurado, escolha um diretório onde o projeto ficará armazenado e via terminal dentro do diretório escolhido podemos fazer o download através do comando <code>git clone https://github.com/chayam/python-fake-api</code>.

# Criando o ambiente virtal e ativando.
Ainda via terminal/prompt/shell navega até o pasta do projeto "python-fake-api" e execute o comando <code>python -m venv venv</code>. Após a criação do ambiente, uma pasta chamada "venv" (ou nome que você definiu) terá sido criada dentro do seu projeto. Vamos ativar o ambiente com o comando para windowns <code>venv\Scripts\activate.bat</code> para linux ou mac <code>source venv/bin/activate</code> via terminal.  

# Instalando bibliotecas
Com ambiente ativado vamos instalar as bibliotecas. As libs estão dentro do arquivo <code>requeriments.txt</code>, para facilitar vamos executar o comando <code>pip install -r requirements.txt</code> que instalará todas as dependencias contidas no arquivo.

# API Utilizada
<b>URL</b>: <a href="https://jsonplaceholder.typicode.com/todos" target="_blank"> https://jsonplaceholder.typicode.com/todos</a><br/>
<b>Método</b>: <code>GET</code> <br/>
<b>Credencial</b>: <code>NÃO</code>


# Executando o projeto.
Com as devidas libs instaladas e projeto com ambiente ativo, vamos executar o projeto. Se estiver usando uma IDE(Vs code,etc) Você pode selecionar o arquivo main.py e compilar direto da ferramenta. Se preferir pode executar via terminal no diretório do projeto e com o ambiente virtual ativo o seguinte comando <code>python main.py</code>. Se tudo ocorrer bem, o projeto estará rodando na url <code>http://127.0.0.1:8082</code>.

<br/>
Obs: Caso você já tenha algum serviço rodando nessa porta, mude no arquivo <code>main.py</code> e procure a linha <code>app.run(host='127.0.0.1', port=8082, debug=True)</code>. Mude para porta que deseja e compile novamente o projeto.

# Rotas do projeto.
<b>rota1:</b> <code>http://localhost:8082/all</code> <br/>
Essa rota consome uma API pulbica via <code>GET</code>, onde atualmente contém 200 registros. basicamente buscamos os dados que estão no formato JSON e convertemos para um Dataframe através da biblioteca pandas. Após convertemos para um DF, exibimos os resultados no navegador em uma tabela HTML (uma das funções do pandas faz essa conversão). 
<br/><br/>
<b>rota2:</b> <code>http://localhost:8082/filter/true/like</code> <br/>
Essa rota consome uma API pulbica via <code>GET</code>, onde atualmente contém 200 registros. Nessa  rota perceba na url após a palavra <code>filter</code> temos mais 2 palavras, que na verdade são parametros. Como funciona? Como exemplo, onde está a palavra <code>true</code> significa <b>o que você deseja buscar dentro do datraframe</b>, e a palavra <code>like</code> é o tipo de busca, podendo ser like ou start.<br/>

<b>Exemplo1</b>: <code>http://localhost:8082/filter/fugiat/start</code> <br/>
Neste exemplo quero buscar todas as palavras que <b>COMEÇAM</b> com a palavra <code>lorem</code> <br/><br/>

<b>Exemplo2</b>: <code>http://localhost:8082/filter/true/like</code> <br/>
Neste exemplo quero buscar todos registros que <b>CONTÉM</b> o valor <code>true</code> <br/><br/>