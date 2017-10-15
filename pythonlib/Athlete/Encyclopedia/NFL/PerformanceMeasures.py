import logging

class PerformanceMeasures(Athlete.Encyclopedia.PerformanceMeasures):
	'''A class for encapsulating the attribute scores for an athlete.'''
	
	def __init__(self):

		self._logger = logging.getLogger(__name__)

		self._lookup = {}

		self._logger.info("Instantiated Athlete.Encyclopedia.NFL.PerformanceMeasures")