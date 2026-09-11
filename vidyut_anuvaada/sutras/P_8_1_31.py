# Sutra प.8.1.31: नह प्रत्यारम्भे
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.31"
SUTRA_TEXT = "नह प्रत्यारम्भे"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.31: अग्निः'),
		('रामः', '', 'प.8.1.31: रामः'),
		('सीता', '', 'प.8.1.31: सीता'),
	]

