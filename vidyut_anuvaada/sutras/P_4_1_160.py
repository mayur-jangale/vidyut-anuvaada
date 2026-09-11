# Sutra प.4.1.160: प्राचामवृद्धात् फिन् बहुलम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prAcAmavfdDAt Pin bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.160"
SUTRA_TEXT = "प्राचामवृद्धात् फिन् बहुलम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prAcAmavfdDAt Pin bahulam"


class Sutra41160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

