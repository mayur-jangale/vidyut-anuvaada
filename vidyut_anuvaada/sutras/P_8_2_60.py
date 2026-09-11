# Sutra प.8.2.60: ऋणमाधमर्ण्ये
# (Final transformations (tripāḍī)) — fRamADamarRye

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.60"
SUTRA_TEXT = "ऋणमाधमर्ण्ये"
SUTRA_DESC = "(Final transformations (tripāḍī)) — fRamADamarRye"


class Sutra8260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.60: अग्निः'),
		('रामः', '', 'प.8.2.60: रामः'),
		('सीता', '', 'प.8.2.60: सीता'),
	]

