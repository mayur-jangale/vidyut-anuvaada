# Sutra प.4.1.153: उदीचामिञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — udIcAmiY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.153"
SUTRA_TEXT = "उदीचामिञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — udIcAmiY"


class Sutra41153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

