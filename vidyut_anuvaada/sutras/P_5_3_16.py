# Sutra प.5.3.16: इदमो र्हिल्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamo rhil

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.16"
SUTRA_TEXT = "इदमो र्हिल्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamo rhil"


class Sutra5316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.16: अग्निः'),
		('रामः', '', 'प.5.3.16: रामः'),
		('सीता', '', 'प.5.3.16: सीता'),
	]

