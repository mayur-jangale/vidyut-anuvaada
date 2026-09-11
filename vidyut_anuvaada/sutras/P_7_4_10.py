# Sutra प.7.4.10: ऋतश्च संयोगादेर्गुणः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.10"
SUTRA_TEXT = "ऋतश्च संयोगादेर्गुणः"
SUTRA_DESC = "taddhita — continued"


class Sutra7410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.10: अग्निः'),
		('रामः', '', 'प.7.4.10: रामः'),
		('सीता', '', 'प.7.4.10: सीता'),
	]

