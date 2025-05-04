<h1>💬 Challenge #1 - Experiência Conversacional FURIA</h1></br>
O projeto faz parte de um desafio desenvolvido pela Furia para vaga de Assistente de Engenharia de Software. 
O objetivo deste primeiro desafio é de criar um Chatbot interativo onde o usuário pode acessar informações sobre o time de CS da Furia.</br></br>

Desenvolvi o projeto utilizando o Python, com a biblioteca telebot e o criador de bot do telegram BotFather.</br>
Motivação: Para esse tipo de serviço a melhor opção que visualizei foi criar um chatbot pelo Telegram, pois é uma rede de facil acesso e permite facil usabilidade, precisando de poucos cliques para chegar no resultado.

**Link do projeto:** <a href=“t.me/furiateamfan_bot/“>FurIA</a>
## 1-Funcionalidades

O bot oferece as seguintes funcionalidades:
- **Próximo Jogo**: Exibe informações sobre o próximo jogo da FURIA.
- **Elenco**: Exibe a lista de jogadores, reservas e comissão técnica.
- **História**: Fornece um resumo da história e principais marcos da FURIA.
- **Redes Sociais**: Links para as redes sociais da organização.
- **Comandos Interativos**: O bot responde aos comandos `/start`, `/help`, `/comandos` e outras mensagens interativas, utilizando um teclado personalizado.

## 2-Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada.
- **Telebot**: Biblioteca para criação de bots no Telegram.
- **BotFather**: Criador de bots do Telegram.
  
## 3-Estrutura do Projeto
  O projeto possui uma pasta para as imagens e um arquivo principal .py com todo o código

## 4-Instalação e Execução
1. Clonar o Repositório
Clone o repositório para sua máquina local:</br>
`git clone https://github.com/vitorss65/DesafiosFuria.git`</br>
`cd DesafiosFuria/FuriaBot`</br>

2. Criação do Bot via BotFather</br>
Acesse o BotFather pelo link: https://telegram.me/BotFather</br>
Siga os comandos que ele orientar para criar o bot e lembre de copiar o Token e o link do seu Chatbot</br>

3. Inserir o Token do Bot</br>
Abra o arquivo furia_bot.py e substitua a string "token" pela chave do seu bot no Telegram:</br>
`TOKEN = "token"`</br>

4. Instalar as Dependências</br>
Instale o pacote necessário com o seguinte comando:
`pip install pyTelegramBotAPI`

6. Executar o Bot
Para iniciar o bot, utilize o comando abaixo no terminal:
`python furia_bot.py`

## 5-Visão Geral do Código
**1.Importações e Inicialização do Bot**
```
import telebot
from telebot import types

TOKEN = "token" 
bot = telebot.TeleBot(TOKEN)
```
-`telebot`: biblioteca usada para criar bots do Telegram.</br>
-`types`: usada para criar botões personalizados.</br>
-`TOKEN`: é a chave que o Telegram fornece para o seu bot funcionar.</br>
-`bot`: objeto principal para controlar e responder mensagens.</br>

**2.Mensagens de Texto**
São definidas em variáveis como:
```
PROXIMO_JOGO = """..."""
JOGADORES = """..."""
```
**3.Teclado Personalizado**
```
def criar_teclado():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('⬅️ Próximo Jogo', '👥 Jogadores')
    markup.row('📜 História', '🔊 Redes Sociais')
    markup.row('❓ Comandos')
    return markup
```
- Cria botões visíveis para o usuário clicar em vez de digitar os comandos </br>

**4.Interpretação**
  ```
  @bot.message_handler(func=lambda msg: True)
  def responder(message):
    texto = message.text.lower()
    
    if 'próximo' in texto or 'jogo' in texto or '/jogos' in texto:
        bot.reply_to(message, PROXIMO_JOGO, ...)
    ...
  ```
  Essa parte interpreta qualquer texto que o usuário mandar, verifica que contém as palavras chaves e em caso positivo
  retorna a mensagem usando `bot.reply_to().`</br>

**5.Iniciando o Bot**
```
print("Bot FurIA operando!")
bot.polling()
```
  `bot.polling()`: mantém o bot esperando por novas mensagens e as respondendo automaticamente. </br>
  
**Comandos e Funcionalidades:**</br>
- `/start, /help, /ajuda`: Envia uma mensagem de boas-vindas com um menu de botões.
- `/comandos`: Reexibe a mensagem com os comandos disponíveis.
- `/jogos` ou botão "Próximo Jogo": Mostra informações sobre a próxima partida da FURIA.
- `/elenco` ou botão "Jogadores": Mostra o elenco atual e a comissão técnica.
- `/historia` ou botão "História": Exibe a trajetória da FURIA Esports.
- `/redes` ou botão "Redes Sociais": Mostra links oficiais da organização.


**Bibliotecas Utilizadas**</br>
- telebot (pyTelegramBotAPI): Interação com a API do Telegram.
- types (do telebot): Para construir o teclado customizado.

**Testes**
O bot pode ser testado diretamente no Telegram após ser iniciado localmente com o comando `python furia_bot.py`. Basta enviar comandos para o bot e verificar as respostas.

**Deploy**
Para fazer o deploy eu utilizei o PythonAnywhere por ser uma opção simples e gratuita, porém </br>


**<h2>Contato</h2>**
Criado por Vitor de Souza Silva</br>
📧 Email: vitorszsilva64@gmail.com</br>
🔗 GitHub: github.com/vitorss65</br>


