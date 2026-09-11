# Sutra प.6.3.39: वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.39"
SUTRA_TEXT = "वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.39: अग्निः'),
		('रामः', '', 'प.6.3.39: रामः'),
		('सीता', '', 'प.6.3.39: सीता'),
	]

