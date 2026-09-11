# Sutra प.4.1.173: साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sAlvAvayavapratyagraTakalakUwASmakAdiY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.173"
SUTRA_TEXT = "साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sAlvAvayavapratyagraTakalakUwASmakAdiY"


class Sutra41173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

