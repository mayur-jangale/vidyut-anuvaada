# Sutra प.7.3.19: हृद्भगसिन्ध्वन्ते पूर्वपदस्य च
# (Taddhita (secondary derivations)) — hfdBagasinDvante pUrvapadasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.19"
SUTRA_TEXT = "हृद्भगसिन्ध्वन्ते पूर्वपदस्य च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hfdBagasinDvante pUrvapadasya ca"


class Sutra7319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.19: अग्निः'),
		('रामः', '', 'प.7.3.19: रामः'),
		('सीता', '', 'प.7.3.19: सीता'),
	]

