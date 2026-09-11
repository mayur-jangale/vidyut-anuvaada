# Sutra प.5.1.78: कालात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.78"
SUTRA_TEXT = "कालात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAt"


class Sutra5178:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.78: अग्निः'),
		('रामः', '', 'प.5.1.78: रामः'),
		('सीता', '', 'प.5.1.78: सीता'),
	]

