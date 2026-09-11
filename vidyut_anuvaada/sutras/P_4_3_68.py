# Sutra प.4.3.68: क्रतुयज्ञेभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kratuyajYeByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.68"
SUTRA_TEXT = "क्रतुयज्ञेभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kratuyajYeByaSca"


class Sutra4368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.68: अग्निः'),
		('रामः', '', 'प.4.3.68: रामः'),
		('सीता', '', 'प.4.3.68: सीता'),
	]

