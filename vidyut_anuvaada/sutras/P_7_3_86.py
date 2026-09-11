# Sutra प.7.3.86: पुगन्तलघूपधस्य च
# (Taddhita (secondary derivations)) — pugantalaGUpaDasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.86"
SUTRA_TEXT = "पुगन्तलघूपधस्य च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pugantalaGUpaDasya ca"


class Sutra7386:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.86: अग्निः'),
		('रामः', '', 'प.7.3.86: रामः'),
		('सीता', '', 'प.7.3.86: सीता'),
	]

