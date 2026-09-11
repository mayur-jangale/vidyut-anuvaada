# Sutra प.2.4.20: संज्ञायां कन्थोशीनरेषु
# (Samasa (compound formation)) — saMjYAyAM kanToSInarezu

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.20"
SUTRA_TEXT = "संज्ञायां कन्थोशीनरेषु"
SUTRA_DESC = "(Samasa (compound formation)) — saMjYAyAM kanToSInarezu"


class Sutra2420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

