# Sutra प.8.2.40: झषस्तथोर्धोऽधः
# (Final transformations (tripāḍī)) — JazastaTorDo'DaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.40"
SUTRA_TEXT = "झषस्तथोर्धोऽधः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — JazastaTorDo'DaH"


class Sutra8240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.40: अग्निः'),
		('रामः', '', 'प.8.2.40: रामः'),
		('सीता', '', 'प.8.2.40: सीता'),
	]

