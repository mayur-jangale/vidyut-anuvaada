# Sutra प.8.2.28: इट ईटि
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.28"
SUTRA_TEXT = "इट ईटि"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.28: अग्निः'),
		('रामः', '', 'प.8.2.28: रामः'),
		('सीता', '', 'प.8.2.28: सीता'),
	]

