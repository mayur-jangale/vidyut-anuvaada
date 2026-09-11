# Sutra प.7.1.58: इदितो नुम् धातोः
# (Taddhita (secondary derivations)) — idito num DAtoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.58"
SUTRA_TEXT = "इदितो नुम् धातोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — idito num DAtoH"


class Sutra7158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.58: अग्निः'),
		('रामः', '', 'प.7.1.58: रामः'),
		('सीता', '', 'प.7.1.58: सीता'),
	]

