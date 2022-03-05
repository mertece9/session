from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Selam {}

Hoş Geldiniz {}

Eğer bu bota güvenmiyorsanız! 
1) Bu iletiyi okumayı durdur. 
2) Bu sohbeti silebilirsin.

Hala okuyor musun?
Pyrogram ve teleton dize oturumu oluşturmak için beni kullanabilirsin. Daha fazla bilgi edinmek için aşağıdaki düğmeleri kullanın! 

> @BotdestekGrubu Tarafından hazırlanmıştır. 
    """

    # Giriş Düğmesi
    home_buttons = [
        [InlineKeyboardButton("🔥 Oturum Oluşturmaya Başla 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Eve Dön 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Oturum Oluşturmaya Başla 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Oturum Oluşturmaya Başla 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Durumu ve Daha Fazla Bot ✨", url="https://t.me/Sohbetdestek")],
        [
            InlineKeyboardButton("Nasıl Kullanılır ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Hakkında 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Daha Şaşırtıcı botlar ♥", url="https://t.me/BotDestekGrubu")],
    ]

    # Help Message
    HELP = """
✨ **Kullanılabilir Komutlar** ✨

/about - Bot Hakkında
/help - Yardım bilgisi için tıkla
/start - Botu Başlatma
/generate - Oturum Oluşturmaya Başlayın
/cancel - İşlemi iptal et
/restart - İşlemi iptal et
"""

    # İleti Hakkında
    ABOUT = """
**Bu Bot Hakkında** 

@BotdestekGrubu Tarafından pyrogram ve telethon dize oturumu oluşturmak için bir telgraf botuyum. 

Kaynak kodu : [Buraya Tıklayın](https://t.me/BotDestekGrubu)

Framework : [Pyrogram](docs.pyrogram.org)

Dil : [Python](www.python.org)

Genel Ekip ve Botlar: @BotdestekGrubu
    """
