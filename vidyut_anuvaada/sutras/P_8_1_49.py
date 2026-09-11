# Sutra प.8.1.49: आहो उताहो चानन्तरम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.49"
SUTRA_TEXT = "आहो उताहो चानन्तरम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.49: अग्निः'),
		('रामः', '', 'प.8.1.49: रामः'),
		('सीता', '', 'प.8.1.49: सीता'),
	]

