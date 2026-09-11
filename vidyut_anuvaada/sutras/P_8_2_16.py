# Sutra प.8.2.16: अनो नुट्
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.16"
SUTRA_TEXT = "अनो नुट्"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8216:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.16: अग्निः'),
		('रामः', '', 'प.8.2.16: रामः'),
		('सीता', '', 'प.8.2.16: सीता'),
	]

