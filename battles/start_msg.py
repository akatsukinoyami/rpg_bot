from pyrogram			import InlineKeyboardMarkup, InlineKeyboardButton
from words.service      import s
from funcs.keyboard     import draw_kb
from classes.battle     import Battle
from lists.enemies      import Enemies

def first_step(app, msg, world):

    enemies         = Enemies()
    world.battle    = Battle(enemies.zhaba)

    txt = f'{s["start_battle"]}, {s["your_enemy"]} - {world.battle.enemy.name}\n'
    txt+= f'{world.battle.enemy.list_characteristics()}\n'
    txt+= f'{world.hero.name}, твои характеристики:\n'
    txt+= world.hero.list_characteristics()
    
    kb = draw_kb([['attack', 'defend'], ['wait', 'leave']])
    
    app.send_message(msg.chat.id, txt, InlineKeyboardMarkup(kb))