# Sutra प.2.3.58: दिवस्तदर्थस्य
# (Samasa (compound formation)) — divastadarTasya

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.58"
SUTRA_TEXT = "दिवस्तदर्थस्य"
SUTRA_DESC = "(Samasa (compound formation)) — divastadarTasya"


class Sutra2358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

