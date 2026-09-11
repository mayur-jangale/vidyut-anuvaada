# Sutra प.8.3.26: हे मपरे वा
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.26"
SUTRA_TEXT = "हे मपरे वा"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.26: अग्निः'),
		('रामः', '', 'प.8.3.26: रामः'),
		('सीता', '', 'प.8.3.26: सीता'),
	]

