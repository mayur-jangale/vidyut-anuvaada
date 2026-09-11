# Sutra प.8.2.20: ग्रो यङि
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.20"
SUTRA_TEXT = "ग्रो यङि"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.20: अग्निः'),
		('रामः', '', 'प.8.2.20: रामः'),
		('सीता', '', 'प.8.2.20: सीता'),
	]

