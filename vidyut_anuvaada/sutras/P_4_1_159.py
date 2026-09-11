# Sutra प.4.1.159: पुत्रान्तादन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — putrAntAdanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.159"
SUTRA_TEXT = "पुत्रान्तादन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — putrAntAdanyatarasyAm"


class Sutra41159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

