# Sutra प.4.1.156: अणो द्व्यचः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aRo dvyacaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.156"
SUTRA_TEXT = "अणो द्व्यचः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aRo dvyacaH"


class Sutra41156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

