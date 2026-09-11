# Sutra प.8.1.17: पदात्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.17"
SUTRA_TEXT = "पदात्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.17: अग्निः'),
		('रामः', '', 'प.8.1.17: रामः'),
		('सीता', '', 'प.8.1.17: सीता'),
	]

