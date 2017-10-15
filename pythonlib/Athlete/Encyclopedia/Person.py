import logging

class Person():
	'''A class for encapsulating an athlete.'''
	
	def __init__(self):

		self._logger = logging.getLogger(__name__)

		self._lookup = {}

		self._logger.info("Instantiated Athlete.Encyclopedia.Person")

	def setFirstName(first_name):
		self._first_name= first_name

	def getFirstName():
		return self._first_name

	def setLastName(last_name):
		self._last_name= last_name

	def getLastName():
		return self._last_name

	def setHeight(h):
		self._height = h

	def getHeight():
		return self._height

	def setWeight(w):
		self._weight = w

	def getWeight():
		return self._weight

	def setArmLength(length):
		self._arm_length = length

	def getArmLength():
		return self._arm_length

	def setHandSize(size):
		self._hand_size = size

	def getHandSize():
		return self._hand_size

	def setPercentBodyFat(fat):
		self._percent_body_fat = fat

	def getPercentBodyFat():
		return self._percent_body_fat
