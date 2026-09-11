# Sutra प.4.4.115: तुग्राद्घन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tugrAdGan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.115"
SUTRA_TEXT = "तुग्राद्घन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tugrAdGan"


class Sutra44115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.115: अग्निः'),
		('रामः', '', 'प.4.4.115: रामः'),
		('सीता', '', 'प.4.4.115: सीता'),
	]

