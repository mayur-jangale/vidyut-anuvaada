# Sutra प.8.3.13: ढो ढे लोपः
# ordīrghājjasaḥ — ओः → दीर्घात् before जस्

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.13"
SUTRA_TEXT = "ढो ढे लोपः"
SUTRA_DESC = "ordīrghājjasaḥ — ओः → दीर्घात् before जस्"


class Sutra8313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.13: अग्निः'),
		('रामः', '', 'प.8.3.13: रामः'),
		('सीता', '', 'प.8.3.13: सीता'),
	]

