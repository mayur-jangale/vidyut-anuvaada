# Sutra प.4.4.124: मायायामण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mAyAyAmaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.124"
SUTRA_TEXT = "मायायामण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mAyAyAmaR"


class Sutra44124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.124: अग्निः'),
		('रामः', '', 'प.4.4.124: रामः'),
		('सीता', '', 'प.4.4.124: सीता'),
	]

