# Sutra प.6.2.16: प्रीतौ च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.16"
SUTRA_TEXT = "प्रीतौ च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6216:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.16: अग्निः'),
		('रामः', '', 'प.6.2.16: रामः'),
		('सीता', '', 'प.6.2.16: सीता'),
	]

