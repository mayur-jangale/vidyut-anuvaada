# Sutra प.6.2.98: सभायां नपुंसके
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.98"
SUTRA_TEXT = "सभायां नपुंसके"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6298:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.98: अग्निः'),
		('रामः', '', 'प.6.2.98: रामः'),
		('सीता', '', 'प.6.2.98: सीता'),
	]

