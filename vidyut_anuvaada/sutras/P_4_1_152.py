# Sutra प.4.1.152: सेनान्तलक्षणकारिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — senAntalakzaRakAriByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.152"
SUTRA_TEXT = "सेनान्तलक्षणकारिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — senAntalakzaRakAriByaSca"


class Sutra41152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

