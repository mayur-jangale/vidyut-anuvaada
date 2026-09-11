# Sutra प.5.1.113: ऐकागारिकट् चौरे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — EkAgArikaw cOre

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.113"
SUTRA_TEXT = "ऐकागारिकट् चौरे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — EkAgArikaw cOre"


class Sutra51113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.113: अग्निः'),
		('रामः', '', 'प.5.1.113: रामः'),
		('सीता', '', 'प.5.1.113: सीता'),
	]

