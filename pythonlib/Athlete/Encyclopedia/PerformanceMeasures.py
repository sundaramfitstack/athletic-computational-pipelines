import logging

class PerformanceMeasures():
	'''A class for encapsulating the performance measures of an athlete.'''
	
	def __init__(self):

		self._logger = logging.getLogger(__name__)

		self._lookup = {}

		self._logger.info("Instantiated Athlete.Encyclopedia.PerformanceMeasures")

	def setDate(date):
		self._date = date

	def getDate():
		return self._date

	def setNoStepVerticalJump(score):
		self._no_step_vertical_jump = score

	def getNoStepVerticalJump():
		return self._no_step_vertical_jump

	def setMaxVerticalJump(score):
		self._max_vertical_jump = score

	def getMaxVerticalJump():
		return self._max_vertical_jump

	def setBenchPress(score):
		self._bench_press = score

	def getBenchPress():
		return self._bench_press

	def setLaneAgility(score):
		self._lane_agility = score

	def getLaneAgility():
		return self._lane_agility

	def setCourtSprint(score):
		self._court_sprint = score

	def getCourtSprint():
		return self._court_sprint

	def setMaxVerticalJump(score):
		self._max_vertical_jump = score

	def getMaxVerticalJump():
		return self._max_vertical_jump

	def setProjected40YardDash(score):
		self._projected_40_yard_dash = score

	def getProjected40YardDash():
		return self._projected_40_yard_dash

	def setProjected100YardDash(score):
		self._projected_100_yard_dash = score

	def getProjected100YardDash():
		return self._projected_100_yard_dash
