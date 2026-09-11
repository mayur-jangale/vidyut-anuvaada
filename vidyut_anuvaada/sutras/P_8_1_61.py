# Sutra प.8.1.61: अहेति विनियोगे च
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.61"
SUTRA_TEXT = "अहेति विनियोगे च"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.61: अग्निः'),
		('रामः', '', 'प.8.1.61: रामः'),
		('सीता', '', 'प.8.1.61: सीता'),
	]

