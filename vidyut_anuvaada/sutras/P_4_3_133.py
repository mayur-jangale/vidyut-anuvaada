# Sutra प.4.3.133: आथर्वणिकस्येकलोपश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ATarvaRikasyekalopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.133"
SUTRA_TEXT = "आथर्वणिकस्येकलोपश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ATarvaRikasyekalopaSca"


class Sutra43133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.133: अग्निः'),
		('रामः', '', 'प.4.3.133: रामः'),
		('सीता', '', 'प.4.3.133: सीता'),
	]

