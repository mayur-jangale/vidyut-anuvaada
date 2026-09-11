# Sutra प.6.2.78: गोतन्तियवं पाले
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.78"
SUTRA_TEXT = "गोतन्तियवं पाले"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6278:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.78: अग्निः'),
		('रामः', '', 'प.6.2.78: रामः'),
		('सीता', '', 'प.6.2.78: सीता'),
	]

