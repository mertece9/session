from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """**
Selam {}

Hoş Geldiniz {}

Pyrogram ve teleton dize oturumu oluşturmak için beni kullanabilirsin. Daha fazla bilgi edinmek için aşağıdaki düğmeleri kullanın! 

> @StarBotKanal Tarafından hazırlanmıştır. 
    """

    # Giriş Düğmesi
    home_buttons = [
        [InlineKeyboardButton("✅ Oturum Oluşturmaya Başla ", callback_data="generate")],
        [InlineKeyboardButton(text="< Geri >", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("✅ Oturum Oluşturmaya Başla ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✅ Oturum Oluşturmaya Başla ", callback_data="generate")],
        [InlineKeyboardButton("🇹🇷 Resmi Kanal", url="https://t.me/StarBotKanal")],
    ]

    # Help Message
    HELP = """
✨ **Kullanılabilir Komutlar** ✨

/about - Bot Hakkında Bilgi
/help - Yardım bilgisi için tıkla
/start - Botu Başlat
/generate - Oturum Oluştur
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
