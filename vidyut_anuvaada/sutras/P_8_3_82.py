# Sutra प.8.3.82: अग्नेः स्तुत्स्तोमसोमाः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.82"
SUTRA_TEXT = "अग्नेः स्तुत्स्तोमसोमाः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8382:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.82: अग्निः'),
		('रामः', '', 'प.8.3.82: रामः'),
		('सीता', '', 'प.8.3.82: सीता'),
	]

