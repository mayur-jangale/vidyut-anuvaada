# Sutra प.6.2.27: आदिः प्रत्येनसि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.27"
SUTRA_TEXT = "आदिः प्रत्येनसि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.27: अग्निः'),
		('रामः', '', 'प.6.2.27: रामः'),
		('सीता', '', 'प.6.2.27: सीता'),
	]

