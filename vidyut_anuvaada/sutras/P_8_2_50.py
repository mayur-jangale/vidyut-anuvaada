# Sutra प.8.2.50: निर्वाणोऽवाते
# (Final transformations (tripāḍī)) — nirvARo'vAte

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.50"
SUTRA_TEXT = "निर्वाणोऽवाते"
SUTRA_DESC = "(Final transformations (tripāḍī)) — nirvARo'vAte"


class Sutra8250:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.50: अग्निः'),
		('रामः', '', 'प.8.2.50: रामः'),
		('सीता', '', 'प.8.2.50: सीता'),
	]

