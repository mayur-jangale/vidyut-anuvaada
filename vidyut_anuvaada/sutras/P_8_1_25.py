# Sutra प.8.1.25: पश्यार्थैश्चानालोचने
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.25"
SUTRA_TEXT = "पश्यार्थैश्चानालोचने"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.25: अग्निः'),
		('रामः', '', 'प.8.1.25: रामः'),
		('सीता', '', 'प.8.1.25: सीता'),
	]

