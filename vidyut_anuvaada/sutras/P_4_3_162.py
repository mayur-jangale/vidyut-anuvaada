# Sutra प.4.3.162: माने वयः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mAne vayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.162"
SUTRA_TEXT = "माने वयः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mAne vayaH"


class Sutra43162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.162: अग्निः'),
		('रामः', '', 'प.4.3.162: रामः'),
		('सीता', '', 'प.4.3.162: सीता'),
	]

