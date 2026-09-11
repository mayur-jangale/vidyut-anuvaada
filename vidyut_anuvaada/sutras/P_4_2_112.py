# Sutra प.4.2.112: इञश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — iYaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.112"
SUTRA_TEXT = "इञश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — iYaSca"


class Sutra42112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.112: अग्निः'),
		('रामः', '', 'प.4.2.112: रामः'),
		('सीता', '', 'प.4.2.112: सीता'),
	]

