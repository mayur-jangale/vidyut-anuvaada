# Sutra प.8.3.67: स्तम्भेः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.67"
SUTRA_TEXT = "स्तम्भेः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.67: अग्निः'),
		('रामः', '', 'प.8.3.67: रामः'),
		('सीता', '', 'प.8.3.67: सीता'),
	]

