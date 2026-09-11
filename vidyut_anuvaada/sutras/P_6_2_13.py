# Sutra प.6.2.13: गन्तव्यपण्यं वाणिजे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.13"
SUTRA_TEXT = "गन्तव्यपण्यं वाणिजे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.13: अग्निः'),
		('रामः', '', 'प.6.2.13: रामः'),
		('सीता', '', 'प.6.2.13: सीता'),
	]

