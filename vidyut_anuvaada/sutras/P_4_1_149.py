# Sutra प.4.1.149: फेश्छ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — PeSCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.149"
SUTRA_TEXT = "फेश्छ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — PeSCa ca"


class Sutra41149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

