# Sutra प.4.2.16: संस्कृतं भक्षाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMskftaM BakzAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.16"
SUTRA_TEXT = "संस्कृतं भक्षाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMskftaM BakzAH"


class Sutra4216:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.16: अग्निः'),
		('रामः', '', 'प.4.2.16: रामः'),
		('सीता', '', 'प.4.2.16: सीता'),
	]

