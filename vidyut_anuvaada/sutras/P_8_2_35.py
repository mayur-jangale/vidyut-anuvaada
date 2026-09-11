# Sutra प.8.2.35: आहस्थः
# paratvaṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.35"
SUTRA_TEXT = "आहस्थः"
SUTRA_DESC = "paratvaṃ — repeated"


class Sutra8235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.35: अग्निः'),
		('रामः', '', 'प.8.2.35: रामः'),
		('सीता', '', 'प.8.2.35: सीता'),
	]

