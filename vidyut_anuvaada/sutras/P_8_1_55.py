# Sutra प.8.1.55: आम एकान्तरमामन्त्रितमनन्तिके
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.55"
SUTRA_TEXT = "आम एकान्तरमामन्त्रितमनन्तिके"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.55: अग्निः'),
		('रामः', '', 'प.8.1.55: रामः'),
		('सीता', '', 'प.8.1.55: सीता'),
	]

