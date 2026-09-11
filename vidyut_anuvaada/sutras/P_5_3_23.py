# Sutra प.5.3.23: प्रकारवचने थाल्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prakAravacane TAl

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.23"
SUTRA_TEXT = "प्रकारवचने थाल्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prakAravacane TAl"


class Sutra5323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.23: अग्निः'),
		('रामः', '', 'प.5.3.23: रामः'),
		('सीता', '', 'प.5.3.23: सीता'),
	]

