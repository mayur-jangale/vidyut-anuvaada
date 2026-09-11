# Sutra प.4.4.17: विभाषा विवधवीवधात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA vivaDavIvaDAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.17"
SUTRA_TEXT = "विभाषा विवधवीवधात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA vivaDavIvaDAt"


class Sutra4417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.17: अग्निः'),
		('रामः', '', 'प.4.4.17: रामः'),
		('सीता', '', 'प.4.4.17: सीता'),
	]

