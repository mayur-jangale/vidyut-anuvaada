# Sutra प.5.2.4: विभाषा तिलमाषोमाभङ्गाऽणुभ्यः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.4"
SUTRA_TEXT = "विभाषा तिलमाषोमाभङ्गाऽणुभ्यः"
SUTRA_DESC = "taddhita — continued"


class Sutra524:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.4: अग्निः'),
		('रामः', '', 'प.5.2.4: रामः'),
		('सीता', '', 'प.5.2.4: सीता'),
	]

