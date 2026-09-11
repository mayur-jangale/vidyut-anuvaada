# Sutra प.6.2.62: ग्रामः शिल्पिनि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.62"
SUTRA_TEXT = "ग्रामः शिल्पिनि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.62: अग्निः'),
		('रामः', '', 'प.6.2.62: रामः'),
		('सीता', '', 'प.6.2.62: सीता'),
	]

