# Sutra प.5.3.5: एतदोऽन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — etado'n

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.5"
SUTRA_TEXT = "एतदोऽन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — etado'n"


class Sutra535:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.5: अग्निः'),
		('रामः', '', 'प.5.3.5: रामः'),
		('सीता', '', 'प.5.3.5: सीता'),
	]

