# Sutra प.2.2.28: तेन सहेति तुल्ययोगे
# (Samasa (compound formation)) — tena saheti tulyayoge

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.28"
SUTRA_TEXT = "तेन सहेति तुल्ययोगे"
SUTRA_DESC = "(Samasa (compound formation)) — tena saheti tulyayoge"


class Sutra2228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

