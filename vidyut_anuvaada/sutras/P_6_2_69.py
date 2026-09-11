# Sutra प.6.2.69: गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.69"
SUTRA_TEXT = "गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6269:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.69: अग्निः'),
		('रामः', '', 'प.6.2.69: रामः'),
		('सीता', '', 'प.6.2.69: सीता'),
	]

