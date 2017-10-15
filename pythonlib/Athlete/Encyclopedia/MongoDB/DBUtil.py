import logging
import pymongo
from pymongo import MongoClient

class DBUtil():
	'''A class for interacting with a MongoDB instance.'''

	_instance = None

	@classmethod
	def getInstance(cls):

		if cls._instance == None:
			cls._instance = DBUtil()

		return cls._instance

	def __init__(self):
		## Insert all connection info here.
		## At some point, should implement support to retrieve mission critical configuration info
		## from configuration file instead of hard-coding here.
		self._logger = logging.getLogger(__name__)

		self._mongo_url = 'mongodb://localhost:3001'
		self._mongo_database_name = 'meteor'
		self._mongo_collection_name = 'analysis'

		self._initMongoClient()

		self._logger.info("Instantiated Athlete.Encyclopedia.MongoDB.DBUtil")


	def _initMongoClient(self):
		''' Instantiate the MongoClient '''

		self._mongo_client = MongoClient(self._mongo_url)

		self._db_handle = self._mongo_client[self._mongo_database_name]

		self._collection = self._db_handle[self._mongo_collection_name]

