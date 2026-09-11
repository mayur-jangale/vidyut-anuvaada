# Sutra प.7.3.29: तत्प्रत्ययस्य च
# (Taddhita (secondary derivations)) — tatpratyayasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.29"
SUTRA_TEXT = "तत्प्रत्ययस्य च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tatpratyayasya ca"


class Sutra7329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.29: अग्निः'),
		('रामः', '', 'प.7.3.29: रामः'),
		('सीता', '', 'प.7.3.29: सीता'),
	]

