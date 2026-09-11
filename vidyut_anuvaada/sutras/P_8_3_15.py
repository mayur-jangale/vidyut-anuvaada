# Sutra प.8.3.15: खरवसानयोर्विसर्जनीयः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.15"
SUTRA_TEXT = "खरवसानयोर्विसर्जनीयः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.15: अग्निः'),
		('रामः', '', 'प.8.3.15: रामः'),
		('सीता', '', 'प.8.3.15: सीता'),
	]

