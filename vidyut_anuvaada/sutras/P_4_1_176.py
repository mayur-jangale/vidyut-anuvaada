# Sutra प.4.1.176: स्त्रियामवन्तिकुन्तिकुरुभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — striyAmavantikuntikuruByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.176"
SUTRA_TEXT = "स्त्रियामवन्तिकुन्तिकुरुभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — striyAmavantikuntikuruByaSca"


class Sutra41176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

