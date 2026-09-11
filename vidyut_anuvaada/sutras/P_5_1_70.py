# Sutra प.5.1.70: स्थालीबिलात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTAlIbilAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.70"
SUTRA_TEXT = "स्थालीबिलात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTAlIbilAt"


class Sutra5170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.70: अग्निः'),
		('रामः', '', 'प.5.1.70: रामः'),
		('सीता', '', 'प.5.1.70: सीता'),
	]

