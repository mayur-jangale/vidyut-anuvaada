# Sutra प.2.2.33: अजाद्यदन्तम्
# (Samasa (compound formation)) — ajAdyadantam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.33"
SUTRA_TEXT = "अजाद्यदन्तम्"
SUTRA_DESC = "(Samasa (compound formation)) — ajAdyadantam"


class Sutra2233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

