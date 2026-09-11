# Sutra प.4.1.162: अपत्यं पौत्रप्रभृति गोत्रम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — apatyaM pOtrapraBfti gotram

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.162"
SUTRA_TEXT = "अपत्यं पौत्रप्रभृति गोत्रम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — apatyaM pOtrapraBfti gotram"


class Sutra41162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

