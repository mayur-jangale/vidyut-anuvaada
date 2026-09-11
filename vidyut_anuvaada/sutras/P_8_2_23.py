# Sutra प.8.2.23: संयोगान्तस्य लोपः
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.23"
SUTRA_TEXT = "संयोगान्तस्य लोपः"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.23: अग्निः'),
		('रामः', '', 'प.8.2.23: रामः'),
		('सीता', '', 'प.8.2.23: सीता'),
	]

