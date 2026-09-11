# Sutra प.8.1.4: नित्यवीप्सयोः
# ṅamo halvādyarthaḥ — ङम् is replaced by हल् in certain contexts

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.4"
SUTRA_TEXT = "नित्यवीप्सयोः"
SUTRA_DESC = "ṅamo halvādyarthaḥ — ङम् is replaced by हल् in certain contexts"


class Sutra814:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.4: अग्निः'),
		('रामः', '', 'प.8.1.4: रामः'),
		('सीता', '', 'प.8.1.4: सीता'),
	]

