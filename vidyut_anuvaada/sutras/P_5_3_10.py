# Sutra प.5.3.10: सप्तम्यास्त्रल्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saptamyAstral

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.10"
SUTRA_TEXT = "सप्तम्यास्त्रल्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saptamyAstral"


class Sutra5310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.10: अग्निः'),
		('रामः', '', 'प.5.3.10: रामः'),
		('सीता', '', 'प.5.3.10: सीता'),
	]

