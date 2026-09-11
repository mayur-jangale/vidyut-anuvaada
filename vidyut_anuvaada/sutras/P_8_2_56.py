# Sutra प.8.2.56: नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्
# (Final transformations (tripāḍī)) — nudavidondatrAGrAhrIByo'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.56"
SUTRA_TEXT = "नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — nudavidondatrAGrAhrIByo'nyatarasyAm"


class Sutra8256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.56: अग्निः'),
		('रामः', '', 'प.8.2.56: रामः'),
		('सीता', '', 'प.8.2.56: सीता'),
	]

