# Sutra प.4.1.171: वृद्धेत्कोसलाजादाञ्ञ्यङ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDetkosalAjAdAYYyaN

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.171"
SUTRA_TEXT = "वृद्धेत्कोसलाजादाञ्ञ्यङ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDetkosalAjAdAYYyaN"


class Sutra41171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

