# Sutra प.4.1.174: ते तद्राजाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — te tadrAjAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.174"
SUTRA_TEXT = "ते तद्राजाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — te tadrAjAH"


class Sutra41174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

