# Sutra प.2.3.60: द्वितीया ब्राह्मणे
# (Samasa (compound formation)) — dvitIyA brAhmaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.60"
SUTRA_TEXT = "द्वितीया ब्राह्मणे"
SUTRA_DESC = "(Samasa (compound formation)) — dvitIyA brAhmaRe"


class Sutra2360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

