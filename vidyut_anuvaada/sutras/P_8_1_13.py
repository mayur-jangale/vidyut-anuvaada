# Sutra प.8.1.13: अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.13"
SUTRA_TEXT = "अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.13: अग्निः'),
		('रामः', '', 'प.8.1.13: रामः'),
		('सीता', '', 'प.8.1.13: सीता'),
	]

