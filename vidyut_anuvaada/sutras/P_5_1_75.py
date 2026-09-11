# Sutra प.5.1.75: पथः ष्कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paTaH zkan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.75"
SUTRA_TEXT = "पथः ष्कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paTaH zkan"


class Sutra5175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.75: अग्निः'),
		('रामः', '', 'प.5.1.75: रामः'),
		('सीता', '', 'प.5.1.75: सीता'),
	]

