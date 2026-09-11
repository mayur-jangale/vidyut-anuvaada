# Sutra प.4.2.42: ब्राह्मणमाणववाडवाद्यन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — brAhmaRamARavavAqavAdyan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.42"
SUTRA_TEXT = "ब्राह्मणमाणववाडवाद्यन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — brAhmaRamARavavAqavAdyan"


class Sutra4242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.42: अग्निः'),
		('रामः', '', 'प.4.2.42: रामः'),
		('सीता', '', 'प.4.2.42: सीता'),
	]

