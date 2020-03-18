from pyrogram			import InlineKeyboardButton
from words.service      import s

def draw_kb(rows):

    keyboard = []
    for oldrow in rows:
        row = []
        for button in oldrow:
            row.append(InlineKeyboardButton(s[button], callback_data=button))
        keyboard.append(row)
    return keyboard