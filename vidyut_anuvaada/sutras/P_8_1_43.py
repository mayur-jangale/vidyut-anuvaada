# Sutra प.8.1.43: नन्वित्यनुज्ञैषणायाम्
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.43"
SUTRA_TEXT = "नन्वित्यनुज्ञैषणायाम्"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.43: अग्निः'),
		('रामः', '', 'प.8.1.43: रामः'),
		('सीता', '', 'प.8.1.43: सीता'),
	]

