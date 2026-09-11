# Sutra प.6.2.75: अणि नियुक्ते
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.75"
SUTRA_TEXT = "अणि नियुक्ते"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6275:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.75: अग्निः'),
		('रामः', '', 'प.6.2.75: रामः'),
		('सीता', '', 'प.6.2.75: सीता'),
	]

