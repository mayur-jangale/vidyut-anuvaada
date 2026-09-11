# Sutra प.4.4.70: अगारान्ताट्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — agArAntAwWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.70"
SUTRA_TEXT = "अगारान्ताट्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — agArAntAwWan"


class Sutra4470:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.70: अग्निः'),
		('रामः', '', 'प.4.4.70: रामः'),
		('सीता', '', 'प.4.4.70: सीता'),
	]

