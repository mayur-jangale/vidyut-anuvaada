# Sutra प.4.1.151: कुर्वादिभ्यो ण्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kurvAdiByo RyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.151"
SUTRA_TEXT = "कुर्वादिभ्यो ण्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kurvAdiByo RyaH"


class Sutra41151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

