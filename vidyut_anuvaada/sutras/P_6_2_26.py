# Sutra प.6.2.26: कुमारश्च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.26"
SUTRA_TEXT = "कुमारश्च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.26: अग्निः'),
		('रामः', '', 'प.6.2.26: रामः'),
		('सीता', '', 'प.6.2.26: सीता'),
	]

