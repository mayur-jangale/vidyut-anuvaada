# Sutra प.4.1.164: भ्रातरि च ज्यायसि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BrAtari ca jyAyasi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.164"
SUTRA_TEXT = "भ्रातरि च ज्यायसि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BrAtari ca jyAyasi"


class Sutra41164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

