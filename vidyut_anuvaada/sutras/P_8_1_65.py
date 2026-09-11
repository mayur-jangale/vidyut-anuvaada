# Sutra प.8.1.65: एकान्याभ्यां समर्थाभ्याम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.65"
SUTRA_TEXT = "एकान्याभ्यां समर्थाभ्याम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.65: अग्निः'),
		('रामः', '', 'प.8.1.65: रामः'),
		('सीता', '', 'प.8.1.65: सीता'),
	]

