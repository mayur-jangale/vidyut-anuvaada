# Sutra प.8.2.38: दधस्तथोश्च
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.38"
SUTRA_TEXT = "दधस्तथोश्च"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.38: अग्निः'),
		('रामः', '', 'प.8.2.38: रामः'),
		('सीता', '', 'प.8.2.38: सीता'),
	]

