# Sutra प.4.1.166: वृद्धस्य च पूजायाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDasya ca pUjAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.166"
SUTRA_TEXT = "वृद्धस्य च पूजायाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDasya ca pUjAyAm"


class Sutra41166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

