# Sutra प.2.4.75: जुहोत्यादिभ्यः श्लुः
# (Samasa (compound formation)) — juhotyAdiByaH SluH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.75"
SUTRA_TEXT = "जुहोत्यादिभ्यः श्लुः"
SUTRA_DESC = "(Samasa (compound formation)) — juhotyAdiByaH SluH"


class Sutra2475:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

