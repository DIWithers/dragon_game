class Hero(object):
	def __init__(self, strength, weapon, health, defense, isAlive, roll, isTurn, purse):
		self.self = self
		self.strength = strength
		self.weapon = weapon
		self.health = health
		self.defense = defense
		self.isAlive = True
		self.roll = roll
		self.isTurn = True
		self.purse = 5

class Dragon(object):
	def __init__(self, strength, health, defense, isAlive, roll, isTurn):
		self.self = self
		self.strength = strength
		self.health = health
		self.defense = defense
		self.isAlive = True
		self.roll = roll
		self.isTurn = False