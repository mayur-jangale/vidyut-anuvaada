# Sutra प.7.3.92: तृणह इम्
# (Taddhita (secondary derivations)) — tfRaha im

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.92"
SUTRA_TEXT = "तृणह इम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tfRaha im"


class Sutra7392:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.92: अग्निः'),
		('रामः', '', 'प.7.3.92: रामः'),
		('सीता', '', 'प.7.3.92: सीता'),
	]

