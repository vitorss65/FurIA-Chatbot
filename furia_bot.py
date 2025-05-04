import telebot
from telebot import types

TOKEN = "7401582647:AAH6hRWssKJPBaAlp6smYKMCdHK8gAs3zP0"
bot = telebot.TeleBot(TOKEN)

PROXIMO_JOGO = """
⚔️ *FURIA vs The MONGOLZ* (CS2)
📅 10/05 - 05:00 (Horário de Brasília)
🏆 PGL Astana 2025
📍 [Assistir na Twitch](https://www.twitch.tv/pgl)
"""


JOGADORES = """
⚔️ *Elenco Principal 2025*:

🕹️ *Jogadores*:
- **MOLODOY** 🇧🇷  
- **YEKINDAR** 🇪🇪  
- **FalleN** 🇧🇷  
- **KSCERATO** 🇧🇷  
- **yuurih** 🇧🇷  

💺 *Reserva*:
- **skullz** 🇧🇷  
- **chelo** 🇧🇷  

📜 *Comissão Técnica*:
- **Coach**: Hepa 🇧🇷  
- **Analista**: sidde 🇧🇷  
"""

HISTORIA = """
📜 <b>História da FURIA</b> 🐆

Fundada em 2017 em São Paulo, a FURIA rapidamente se tornou uma das organizações mais proeminentes de esports do Brasil e do mundo. 
Seu estilo agressivo e ousado de jogar, especialmente em Counter-Strike: Global Offensive (CS:GO), conquistou fãs no mundo todo.

🎯 <b>Missão:</b> Levar o Brasil ao protagonismo global por meio do esporte eletrônico, arte, cultura e impacto social.

🚀 <b>Principais Marcos:</b>
- 2018: Primeira aparição internacional no qualifier para o Major de Londres
- 2019: Estreia em Major (Berlim) com o lendário "FURIA Playstyle" agressivo
- 2020: Mudança para os EUA e conquista de posições no Top 5 mundial
- 2022: Semifinal histórica no IEM Major Rio, com torcida brasileira em peso
- 2023: Ampliação das modalidades: Valorant, LoL, Apex, xadrez e mais

🏟️ <b>Infraestrutura:</b>
- Gaming office em São Paulo
- Centro de treinamento em Miami (EUA)
- Casas de conteúdo, estúdios e arenas de treino

🌎 <b>Impacto:</b>
A FURIA ultrapassa os limites do competitivo e investe em educação, inclusão, performance e lifestyle, sendo referência de inovação no cenário.

🖤 <b>Curiosidades:</b>
- O nome "FURIA" vem da vontade de competir com intensidade e paixão
- A organização possui parcerias com grandes marcas como Red Bull, Adidas, PokerStars, Hellmanm's, entre outras
- É uma das únicas equipes brasileiras a manter line-ups estáveis e investir em formação a longo prazo
"""



# Teclado personalizado
def criar_teclado():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('⬅️ Próximo Jogo', '👥 Jogadores')
    markup.row('📜 História', '🔊 Redes Sociais')
    markup.row('❓ Comandos')
    return markup

#Mensagem de boas-vindas
@bot.message_handler(commands=['start', 'help', 'ajuda'])
def welcome(message):
    # Enviar a imagem junto com a mensagem de boas-vindas como legenda
    welcome_msg = """
🎮 *Bem-vindo ao Bot FurIA!* 🎮

⚡ *Comandos disponíveis:*

• /start - Mensagem de boas-vindas
• /jogos - Próximas partidas
• /elenco - Jogadores e staff
• /historia - Conquistas do time
• /redes - Redes sociais
• /comandos - Lista completa

💡 Você também pode usar os botões abaixo para interagir!
    """
    
    bot.send_photo(
        message.chat.id,
        photo=open('img/furiacs.jpg', 'rb'),  # Caminho relativo da imagem
        caption=welcome_msg,  # A mensagem vai como legenda da foto
        parse_mode='Markdown',  # Formatação em Markdown
        reply_markup=criar_teclado()  # Teclado personalizado
    )


# Reusa a mensagem de boas-vindas
@bot.message_handler(commands=['comandos'])
def show_commands(message):
    welcome(message)  

@bot.message_handler(func=lambda msg: True)
def responder(message):
    texto = message.text.lower()
    
    if 'próximo' in texto or 'jogo' in texto or '/jogos' in texto:
        bot.reply_to(message, PROXIMO_JOGO, parse_mode='Markdown', disable_web_page_preview=False)
    elif 'jogadores' in texto or 'elenco' in texto or '/elenco' in texto:
        bot.reply_to(message, JOGADORES, parse_mode='Markdown')
    elif 'história' in texto or 'historia' in texto or '/historia' in texto:
        bot.reply_to(message, HISTORIA, parse_mode='HTML')
    elif 'redes' in texto or 'social' in texto or '/redes' in texto:
        bot.reply_to(message, 
            "📱 *Redes Sociais Oficiais*:\n"
            "🐦 Twitter: [@FURIA](https://twitter.com/furia)\n"
            "📸 Instagram: [@furiagg](https://instagram.com/furiagg)\n"
            "🎥 YouTube: [FURIA](https://youtube.com/furiagg)\n"
            "💬 Discord: [FURIA GG](https://discord.gg/furia)",
            parse_mode='Markdown'
        )
    elif 'comandos' in texto or 'ajuda' in texto or 'help' in texto:
        welcome(message)
    else:
        bot.reply_to(message, 
                     "🤖 Comando não reconhecido. Use /comandos para ver as opções disponíveis.",
                     reply_markup=criar_teclado())

print("Bot FurIA operando!")
bot.polling()