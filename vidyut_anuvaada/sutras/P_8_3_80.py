# Sutra प.8.3.80: समासेऽङ्गुलेः सङ्गः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.80"
SUTRA_TEXT = "समासेऽङ्गुलेः सङ्गः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.80: अग्निः'),
		('रामः', '', 'प.8.3.80: रामः'),
		('सीता', '', 'प.8.3.80: सीता'),
	]

