# Sutra प.5.3.42: संख्याया विधार्थे धा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA viDArTe DA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.42"
SUTRA_TEXT = "संख्याया विधार्थे धा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA viDArTe DA"


class Sutra5342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.42: अग्निः'),
		('रामः', '', 'प.5.3.42: रामः'),
		('सीता', '', 'प.5.3.42: सीता'),
	]

