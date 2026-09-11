# Sutra प.4.4.68: भक्तादणन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BaktAdaRanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.68"
SUTRA_TEXT = "भक्तादणन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BaktAdaRanyatarasyAm"


class Sutra4468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.68: अग्निः'),
		('रामः', '', 'प.4.4.68: रामः'),
		('सीता', '', 'प.4.4.68: सीता'),
	]

