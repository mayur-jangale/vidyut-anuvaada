# Sutra प.8.2.34: नहो धः
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.34"
SUTRA_TEXT = "नहो धः"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.34: अग्निः'),
		('रामः', '', 'प.8.2.34: रामः'),
		('सीता', '', 'प.8.2.34: सीता'),
	]

