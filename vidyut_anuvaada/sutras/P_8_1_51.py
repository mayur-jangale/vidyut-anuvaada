# Sutra प.8.1.51: गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.51"
SUTRA_TEXT = "गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.51: अग्निः'),
		('रामः', '', 'प.8.1.51: रामः'),
		('सीता', '', 'प.8.1.51: सीता'),
	]

