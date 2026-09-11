# Sutra प.8.1.27: तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.27"
SUTRA_TEXT = "तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.27: अग्निः'),
		('रामः', '', 'प.8.1.27: रामः'),
		('सीता', '', 'प.8.1.27: सीता'),
	]

