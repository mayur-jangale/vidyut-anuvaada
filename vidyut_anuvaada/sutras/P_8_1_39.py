# Sutra प.8.1.39: तुपश्यपश्यताहैः पूजायाम्
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.39"
SUTRA_TEXT = "तुपश्यपश्यताहैः पूजायाम्"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.39: अग्निः'),
		('रामः', '', 'प.8.1.39: रामः'),
		('सीता', '', 'प.8.1.39: सीता'),
	]

