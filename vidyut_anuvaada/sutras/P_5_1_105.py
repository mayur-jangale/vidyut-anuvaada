# Sutra प.5.1.105: ऋतोरण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ftoraR

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.105"
SUTRA_TEXT = "ऋतोरण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ftoraR"


class Sutra51105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.105: अग्निः'),
		('रामः', '', 'प.5.1.105: रामः'),
		('सीता', '', 'प.5.1.105: सीता'),
	]

