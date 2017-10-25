import logging
import sys

class Calculator():
	'''A class for encapsulating the performance calculation forumlas.'''
	
	def __init__(self):

		self._logger = logging.getLogger(__name__)

		self._lookup = {}

		self._logger.info("Instantiated Athlete.Encyclopedia.Performance.Calculator")


	def getPower(self, weight, jump):
		''' -2259+36.49*(weight in lbs/2.2)+6983*(vertical jump inches*0.0254) 

			Parameters are:

			weight (in lbs)

			jump (vertical jump in inches)

		'''

		if not self._is_weight_valid(weight):
			sys.exit(1)

		if not self._is_jump_valid(jump)
			sys.exit(1)

		## Description of values that follow:
		## 
		## 2.2 - convertPoundsToKilo ---> pound to kg conversion
		## 0.0254 - convertInchesToMeters --> inches to meters conversion
		## -2259 - razu1
		## 36.49 - razu2
		## 6983 - razu3

		power = -2259 + 36.49 * (weight/2.2) + 6983 * (jump * 0.0254)

		self._logger.info("Calculated power %d for weight %d and vertical jump %d" % (power, weight, jump))

		return power


	def _is_weight_valid(weight):

		if weight == None:
			self._logger.fatal("weight was not defined")
			raise Exception("weight was not defined")

		if weight < 0:
			self._logger.fatal("weight was '%d'" % weight)
			raise Exception("weight was '%d'" % weight)

	def _is_jump_valid(jump):

		if jump == None:
			self._logger.fatal("jump was not defined")
			raise Exception("jump was not defined")

		if jump < 0:
			self._logger.fatal("jump was '%d'" % jump)
			raise Exception("jump was '%d'" % jump)


	def getEstimated40YardDashTimeFromCourtSprint(sprint_time, weight):
		'''
			parameters are:

			sprint_time (time in seconds for 3/4 court sprint)

			weight (weight in pounds)
		'''

		if not self._is_court_sprint_time_valid(sprint_time):
			sys.exit(1)


		## Est 40yd dash time = [40/(.5*acceleration)]^(.5)] + W
		## acceleration = (2*distance)/(time^2)
		##
		## 40 - estFortyDashConst1
		## 0.5 - estFortyDashConst2
		## 22.86 - threeQuarterCourtDistMeters - the distance of 3/4 court in meters (i.e. 75 feet)
		## 2 - estFortyAccelConst
		## W -  constant that changes based on an athlete's weight as per the following:
		## < 190lbs: W = 0.30
		## 190lbs - 200lbs: W = 0.35
		## 200lbs - 210lbs: W = 0.40
		## 210lbs - 220lbs: W = 0.45
		## 220lbs+: W = .50

		acceleration = (2 * 40)/(sprint_time * sprint_time)

		if weight < 190:
			w_val = 0.30
		else if weight < 201:
			w_val = 0.35
		else if weight < 210:
			w_val = 0.40
		else if weight < 220:
			w_val = 0.45
		else:
			w_val = 0.50


		dash_time = (40/(0.5 * acceleration)^0.5) + w_val

		self._logger.info("Calculated estimated 40 yard dash time '%d' from 3/4 court sprint time '%d' and weight '%d'" % (dash_time, sprint_time, weight))

		return dash_time


	def _is_court_sprint_time_valid(sprint_time):

		if sprint_time == None:
			self._logger.fatal("sprint_time was not defined")
			raise Exception("sprint_time was not defined")

		if sprint_time < 0:
			self._logger.fatal("sprint_time was '%d'" % sprint_time)
			raise Exception("sprint_time was '%d'" % sprint_time)


	def getEstimated100YardDashTimeFrom40YardDashTime(dash_time):
		'''40yd time / 2.54 + 40yd time + 40yd time

			parameters are:

			dash_time (time in seconds for the 40 yard dash)
		'''

		if not self._is_40_yard_dash_time_valid(dash_time):
			sys.exit(1)

		## 2.54 - estHundredMeterConst

		dash_time_100 = dash_time / 2.54 + dash_time + dash_time

		self._logger.info("Calculated 100 yard dash time '%d' from 40 yard dash time '%d'" % (dash_time_100, dash_time))

		return dash_time_100


	def _is_40_yard_dash_time_valid(dash_time):

		if dash_time == None:
			self._logger.fatal("dash_time was not defined")
			raise Exception("dash_time was not defined")

		if dash_time < 0:
			self._logger.fatal("dash_time was '%d'" % dash_time)
			raise Exception("dash_time was '%d'" % dash_time)


	def getAbsoluteStrength(force, weight):
		'''force (weight in lbs/2.2)

			parameters are:

			force

			weight (in lbs)
		'''

		if not self._is_force_valid(force):
			sys.exit(1)


		if not self._is_weight_valid(weight):
			sys.exit(1)

		
		strength = force * weight / 2.2

		self._logger.info("Calculated absolute strength '%d' from force '%d' and weight '%d'" % (strength, force, weight))

		return strength


	def _is_force_valid(force):

		if force == None:
			self._logger.fatal("force was not defined")
			raise Exception("force was not defined")

		if force < 0:
			self._logger.fatal("force was '%d'" % force)
			raise Exception("force was '%d'" % force)


	def getRelativeStrength(force, weight, bodyweight):
		'''force (weight in lbs/2.2) / bodyweight (in lbs/2.2)

			parameters are:

			force

			weight (in lbs)

			bodyweight (in lbs)
		'''

		if not self._is_force_valid(force):
			sys.exit(1)


		if not self._is_weight_valid(weight):
			sys.exit(1)

		if not self._is_bodyweight_valid(bodyweight):
			sys.exit(1)

		
		strength = force (weight/2.2 / bodyweight/2.2)

		self._logger.info("Calculated relative strength '%d' from force '%d' weight '%d' and bodyweight '%d'" % (strength, force, weight, bodyweight))

		return strength


	def _is_bodyweight_valid(bodyweight):

		if bodyweight == None:
			self._logger.fatal("bodyweight was not defined")
			raise Exception("bodyweight was not defined")

		if bodyweight < 0:
			self._logger.fatal("bodyweight was '%d'" % bodyweight)
			raise Exception("bodyweight was '%d'" % bodyweight)


	def getAcceleration(distance, time):
		'''distance (yds*.9144) / time (secs) / time (secs)

			parameters are:

			distance (yards)

			time (seconds)
		'''

		if not self._is_distance_valid(distance):
			sys.exit(1)


		if not self._is_time_valid(time):
			sys.exit(1)

	
		## .9144 - convertYardsToMeters

		acceleration = (distance * 0.9144) / time * time

		self._logger.info("Calculated acceleration '%d' from distance '%d' time '%d'" % (acceleration, distance, time))

		return acceleration


	def _is_distance_valid(distance):

		if distance == None:
			self._logger.fatal("distance was not defined")
			raise Exception("distance was not defined")

		if distance < 0:
			self._logger.fatal("distance was '%d'" % distance)
			raise Exception("distance was '%d'" % distance)


