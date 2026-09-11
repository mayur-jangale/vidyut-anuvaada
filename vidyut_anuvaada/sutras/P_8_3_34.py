# Sutra प.8.3.34: विसर्जनीयस्य सः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.34"
SUTRA_TEXT = "विसर्जनीयस्य सः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.34: अग्निः'),
		('रामः', '', 'प.8.3.34: रामः'),
		('सीता', '', 'प.8.3.34: सीता'),
	]

