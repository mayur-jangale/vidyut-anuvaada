# Sutra प.5.1.117: तदर्हम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadarham

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.117"
SUTRA_TEXT = "तदर्हम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadarham"


class Sutra51117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.117: अग्निः'),
		('रामः', '', 'प.5.1.117: रामः'),
		('सीता', '', 'प.5.1.117: सीता'),
	]

