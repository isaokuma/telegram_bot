# Instruções
Versão Python: 2.7.12


# Criação do bot
Para criar um bot no aplicativo Telegram você é necessário seguir os seguintes passos:
* Clicar no campo de busca do Telegram e pesquisar por ```@BotFather```
* Depois de iniciar uma conversa com o ```@BotFather```enviar a seguinte mensagem:  ```/newbot```
* Após isso, o ```@BotFather``` irá solicitar o nome e o nome de usuário que você deseja dar ao seu bot. Para o nome de usuário existem algumas restrições que devem ser respeitadas. É obrigatório que você escolha um nome de usuário que ainda não existe e o final do nome deve conter ```Bot```
* Depois que o seu bot for criado você receberá um token de acesso, que será utilizado para fazer a conexão entre a API do Telegram e o seu bot. Caso você esqueça dele, você deve enviar o comando ```/token``` para o ```@BotFather```




# Instalação de módulos

Para nos conectarmos ao bot que criamos usando o BotFather será utilizado o módulo telepot. Este módulo faz a conexão do nosso programa com a API de bots do Telegram.

Antes de poder fazer a utilização desse módulo, deve ser instalado o gerenciador de pacotes da linguagem Python (pip):
```
pip install -U pip
sudo apt install python3-pip
```
Após isso, podemos fazer a instalação e/ou atualização do módulo através dos seguintes comandos: 

* Instalação utilizando o pip ou pip3

```
			pip install telepot 
			pip3 install telepot
```      

* Atualização utilizando o pip ou pi3

```
			pip install telepot –upgrade 
			pip3 install telepot --upgrade
```
Feito isso, o módulo já estará pronto para ser utilizado!


# Execução do código

Explicação
