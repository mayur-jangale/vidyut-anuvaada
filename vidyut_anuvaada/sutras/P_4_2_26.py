# Sutra प.4.2.26: शुक्राद्घन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SukrAdGan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.26"
SUTRA_TEXT = "शुक्राद्घन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SukrAdGan"


class Sutra4226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.26: अग्निः'),
		('रामः', '', 'प.4.2.26: रामः'),
		('सीता', '', 'प.4.2.26: सीता'),
	]

