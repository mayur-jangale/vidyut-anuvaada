# Sutra प.5.1.21: शताच्च ठन्यतावशते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatAcca WanyatAvaSate

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.21"
SUTRA_TEXT = "शताच्च ठन्यतावशते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatAcca WanyatAvaSate"


class Sutra5121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.21: अग्निः'),
		('रामः', '', 'प.5.1.21: रामः'),
		('सीता', '', 'प.5.1.21: सीता'),
	]

