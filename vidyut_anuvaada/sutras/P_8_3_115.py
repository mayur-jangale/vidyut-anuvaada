# Sutra प.8.3.115: सोढः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.115"
SUTRA_TEXT = "सोढः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.115: अग्निः'),
		('रामः', '', 'प.8.3.115: रामः'),
		('सीता', '', 'प.8.3.115: सीता'),
	]

