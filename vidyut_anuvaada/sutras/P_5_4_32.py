# Sutra प.5.4.32: रक्ते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rakte

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.32"
SUTRA_TEXT = "रक्ते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rakte"


class Sutra5432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.32: अग्निः'),
		('रामः', '', 'प.5.4.32: रामः'),
		('सीता', '', 'प.5.4.32: सीता'),
	]

