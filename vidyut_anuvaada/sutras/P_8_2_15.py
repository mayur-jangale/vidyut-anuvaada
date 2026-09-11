# Sutra प.8.2.15: छन्दसीरः
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.15"
SUTRA_TEXT = "छन्दसीरः"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.15: अग्निः'),
		('रामः', '', 'प.8.2.15: रामः'),
		('सीता', '', 'प.8.2.15: सीता'),
	]

