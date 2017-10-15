import logging

class Manager():
	'''A class for orchestrating API tasks'''

	_instance = None

	@classmethod
	def getInstance(cls):

		if cls._instance == None:
			cls._instance = Manager()	

		return cls._instance


	def __init__(self):
		
		self._logger = logging.getLogger(__name__)
				
		self._logger.info("Instantiated Athlete.Encyclopedia.Manager")


	def setIndir(self, indir):
		self._indir = indir
	
	def setOutdir(self, outdir)	:
		self._outdir = outdir

	def run(self):
		pass