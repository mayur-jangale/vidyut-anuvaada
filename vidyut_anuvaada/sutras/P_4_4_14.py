# Sutra प.4.4.14: आयुधाच्छ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AyuDAcCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.14"
SUTRA_TEXT = "आयुधाच्छ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AyuDAcCa ca"


class Sutra4414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.14: अग्निः'),
		('रामः', '', 'प.4.4.14: रामः'),
		('सीता', '', 'प.4.4.14: सीता'),
	]

