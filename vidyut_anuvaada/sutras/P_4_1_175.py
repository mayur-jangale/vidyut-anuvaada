# Sutra प.4.1.175: कम्बोजाल्लुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kambojAlluk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.175"
SUTRA_TEXT = "कम्बोजाल्लुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kambojAlluk"


class Sutra41175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

