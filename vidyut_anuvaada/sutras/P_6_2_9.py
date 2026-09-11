# Sutra प.6.2.9: शारदेऽनार्तवे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.9"
SUTRA_TEXT = "शारदेऽनार्तवे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra629:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.9: अग्निः'),
		('रामः', '', 'प.6.2.9: रामः'),
		('सीता', '', 'प.6.2.9: सीता'),
	]

