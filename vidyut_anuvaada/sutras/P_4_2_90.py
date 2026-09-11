# Sutra प.4.2.90: उत्करादिभ्यश्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — utkarAdiByaSCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.90"
SUTRA_TEXT = "उत्करादिभ्यश्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — utkarAdiByaSCaH"


class Sutra4290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.90: अग्निः'),
		('रामः', '', 'प.4.2.90: रामः'),
		('सीता', '', 'प.4.2.90: सीता'),
	]

