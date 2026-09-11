# Sutra प.8.3.116: स्तम्भुसिवुसहां चङि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.116"
SUTRA_TEXT = "स्तम्भुसिवुसहां चङि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.116: अग्निः'),
		('रामः', '', 'प.8.3.116: रामः'),
		('सीता', '', 'प.8.3.116: सीता'),
	]

