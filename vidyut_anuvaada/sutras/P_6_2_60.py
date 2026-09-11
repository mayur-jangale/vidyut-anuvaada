# Sutra प.6.2.60: षष्ठी प्रत्येनसि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.60"
SUTRA_TEXT = "षष्ठी प्रत्येनसि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.60: अग्निः'),
		('रामः', '', 'प.6.2.60: रामः'),
		('सीता', '', 'प.6.2.60: सीता'),
	]

