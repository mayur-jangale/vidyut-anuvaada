# Sutra प.6.2.49: गतिरनन्तरः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.49"
SUTRA_TEXT = "गतिरनन्तरः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.49: अग्निः'),
		('रामः', '', 'प.6.2.49: रामः'),
		('सीता', '', 'प.6.2.49: सीता'),
	]

