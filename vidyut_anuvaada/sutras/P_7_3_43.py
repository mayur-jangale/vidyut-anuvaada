# Sutra प.7.3.43: रुहः पोऽन्यतरस्याम्
# (Taddhita (secondary derivations)) — ruhaH po'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.43"
SUTRA_TEXT = "रुहः पोऽन्यतरस्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ruhaH po'nyatarasyAm"


class Sutra7343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.43: अग्निः'),
		('रामः', '', 'प.7.3.43: रामः'),
		('सीता', '', 'प.7.3.43: सीता'),
	]

