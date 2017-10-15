import logging

class AttributeScores(Person):
	'''A class for encapsulating the attribute scores for an athlete.'''
	
	def __init__(self):

		self._logger = logging.getLogger(__name__)

		self._lookup = {}

		self._logger.info("Instantiated Athlete.Encyclopedia.AttributeScores")

	def setDate(date):
		self._date = date

	def getDate():
		return self._date

	def setAbsoluteStrength(score):
		self._absolute_strength = score

	def getAbsoluteStrength():
		return self._absolute_strength

	def setRelativeStrength(score):
		self._relative_strength = score

	def getRelativeStrength():
		return self._relative_strength

	def setAllometricStrength(score):
		self._allometric_strength = score

	def getAllometricStrength():
		return self._allometric_strength

	def setPower(score):
		self._power = score

	def getPower():
		return self._power

	def setSpeed(score):
		self._speed = score

	def getSpeed():
		return self._speed

	def setAcceleration(score):
		self._acceleration = score

	def getAcceleration():
		return self._acceleration

	def setAgility(score):
		self._agility = score

	def getAgility():
		return self._agility

	def setBodyComposition(score):
		self._body_composition = score

	def getBodyComposition():
		return self._body_composition

	def setOverall(score):
		self._overall = score

	def getOverall():
		return self._overall







