from pyrogram 			import Client, Filters
import shelve
from classes.world		import World
from battles.start_msg	import first_step

with shelve.open('rpgbotDB') as db:
	app = Client("rpgbot")

	def db_decorator(my_func):
		def wrapper(app, msg):
			user		= msg.from_user
			username	= user.first_name
			user_id	    = user.id
			if user_id not in db:
				db[user_id] = World(username)
			world = db[user_id]

			my_func(app, msg, world)

			db[user_id] = world
			db.sync() 
			msg.continue_propagation() 
		return wrapper

	@app.on_message(~Filters.channel, Filters.command('game'))
	@db_decorator
	def open_game(app, msg, world):
		start(app, msg, world)