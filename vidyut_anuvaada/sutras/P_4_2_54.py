# Sutra प.4.2.54: भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BOrikyAdyEzukAryAdiByo viDalBaktalO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.54"
SUTRA_TEXT = "भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BOrikyAdyEzukAryAdiByo viDalBaktalO"


class Sutra4254:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.54: अग्निः'),
		('रामः', '', 'प.4.2.54: रामः'),
		('सीता', '', 'प.4.2.54: सीता'),
	]

