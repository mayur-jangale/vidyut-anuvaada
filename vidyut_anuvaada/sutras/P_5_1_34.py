# Sutra प.5.1.34: पणपादमाषशताद्यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paRapAdamAzaSatAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.34"
SUTRA_TEXT = "पणपादमाषशताद्यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paRapAdamAzaSatAdyat"


class Sutra5134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.34: अग्निः'),
		('रामः', '', 'प.5.1.34: रामः'),
		('सीता', '', 'प.5.1.34: सीता'),
	]

