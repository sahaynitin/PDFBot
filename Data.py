from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can help you to do stuff on Pdfs as well as convert images to Pdf. Use /help command to see features.

JUST SEND A PDF (or an image) to get started.

Made With 💕 By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏡 Return Home", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📡 Update Channel", url="https://t.me/tellybots_4u")],
        [
            InlineKeyboardButton("How to Use me ❔", callback_data="help"),
            InlineKeyboardButton("👲 About", callback_data="about")
        ],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/Tellybots_support")],
    ]

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot with Pdf tools by @Tellybots_4u

Source Code : [Click Here](https://t.me/tellybots_digital)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developed By : @Tellybots_4u
    """
