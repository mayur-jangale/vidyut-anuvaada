# Sutra प.4.1.1: ङ्याप्प्रातिपदिकात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — NyApprAtipadikAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.1"
SUTRA_TEXT = "ङ्याप्प्रातिपदिकात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — NyApprAtipadikAt"


class Sutra411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

