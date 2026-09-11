# Sutra प.8.1.37: पूजायां नानन्तरम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.37"
SUTRA_TEXT = "पूजायां नानन्तरम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.37: अग्निः'),
		('रामः', '', 'प.8.1.37: रामः'),
		('सीता', '', 'प.8.1.37: सीता'),
	]

