# Sutra प.6.2.63: राजा च प्रशंसायाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.63"
SUTRA_TEXT = "राजा च प्रशंसायाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.63: अग्निः'),
		('रामः', '', 'प.6.2.63: रामः'),
		('सीता', '', 'प.6.2.63: सीता'),
	]

