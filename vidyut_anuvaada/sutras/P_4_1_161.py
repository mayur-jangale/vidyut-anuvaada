# Sutra प.4.1.161: मनोर्जातावञ्यतौ षुक् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — manorjAtAvaYyatO zuk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.161"
SUTRA_TEXT = "मनोर्जातावञ्यतौ षुक् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — manorjAtAvaYyatO zuk ca"


class Sutra41161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

