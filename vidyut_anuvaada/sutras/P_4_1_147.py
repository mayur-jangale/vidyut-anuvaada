# Sutra प.4.1.147: गोत्रस्त्रियाः कुत्सने ण च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gotrastriyAH kutsane Ra ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.147"
SUTRA_TEXT = "गोत्रस्त्रियाः कुत्सने ण च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gotrastriyAH kutsane Ra ca"


class Sutra41147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

