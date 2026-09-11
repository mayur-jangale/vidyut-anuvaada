# Sutra प.8.2.93: विभाषा पृष्टप्रतिवचने हेः
# (Final transformations (tripāḍī)) — viBAzA pfzwaprativacane heH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.93"
SUTRA_TEXT = "विभाषा पृष्टप्रतिवचने हेः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — viBAzA pfzwaprativacane heH"


class Sutra8293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.93: अग्निः'),
		('रामः', '', 'प.8.2.93: रामः'),
		('सीता', '', 'प.8.2.93: सीता'),
	]

