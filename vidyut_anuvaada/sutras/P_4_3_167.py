# Sutra प.4.3.167: हरीतक्यादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — harItakyAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.167"
SUTRA_TEXT = "हरीतक्यादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — harItakyAdiByaSca"


class Sutra43167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.167: अग्निः'),
		('रामः', '', 'प.4.3.167: रामः'),
		('सीता', '', 'प.4.3.167: सीता'),
	]

