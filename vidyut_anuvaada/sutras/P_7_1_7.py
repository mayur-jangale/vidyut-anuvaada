# Sutra प.7.1.7: वेत्तेर्विभाषा
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.7"
SUTRA_TEXT = "वेत्तेर्विभाषा"
SUTRA_DESC = "taddhita — continued"


class Sutra717:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.7: अग्निः'),
		('रामः', '', 'प.7.1.7: रामः'),
		('सीता', '', 'प.7.1.7: सीता'),
	]

