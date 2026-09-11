# Sutra प.4.2.61: क्रमादिभ्यो वुन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kramAdiByo vun

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.61"
SUTRA_TEXT = "क्रमादिभ्यो वुन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kramAdiByo vun"


class Sutra4261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.61: अग्निः'),
		('रामः', '', 'प.4.2.61: रामः'),
		('सीता', '', 'प.4.2.61: सीता'),
	]

