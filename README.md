# Instruções
Versão Python: 2.7.12


# Criação do bot

Para podermos criar um bot que conecte-se com o Telegram é preciso do @BotFather. Para fazer a criação, envie o seguinte comando para o mesmo: "/newbot"

Após isso, o BotFather irá solicitar o nome que você deseja dar ao seu bot. É preciso lembrar que no final do nome é obrigatório conter “bot”. Por exemplo: TesteBot

Depois que o seu bot for criado você receberá um token de acesso, que será utilizado para fazer a conexão entre a API do Telegram e o seu bot. Caso você esqueça dele, você deve enviar o comando "/token" para o BotFather.

# Instalação de módulos

Para nos conectarmos ao bot que criamos usando o BotFather será utilizado o módulo telepot. Este módulo faz a conexão do nosso programa com a API de bots do Telegram.

Antes de poder fazer a utilização desse módulo, deve ser instalado o gerenciador de pacotes da linguagem Python (pip):
```
pip install -U pip
```
Após isso, podemos fazer a instalação e/ou atualização do módulo através dos seguintes comandos: 

* Instalação

```
			pip install telepot 
```      
OU
```
			pip3 install telepot
```      

* Atualização

```
			pip install telepot –upgrade 
```
OU
```
			pip3 install telepot --upgrade
```      
