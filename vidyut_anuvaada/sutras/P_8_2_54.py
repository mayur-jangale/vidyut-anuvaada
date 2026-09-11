# Sutra प.8.2.54: प्रस्त्योऽन्यतरस्याम्
# (Final transformations (tripāḍī)) — prastyo'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.54"
SUTRA_TEXT = "प्रस्त्योऽन्यतरस्याम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — prastyo'nyatarasyAm"


class Sutra8254:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.54: अग्निः'),
		('रामः', '', 'प.8.2.54: रामः'),
		('सीता', '', 'प.8.2.54: सीता'),
	]

