# Sutra प.4.2.37: तस्य समूहः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasya samUhaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.37"
SUTRA_TEXT = "तस्य समूहः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasya samUhaH"


class Sutra4237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.37: अग्निः'),
		('रामः', '', 'प.4.2.37: रामः'),
		('सीता', '', 'प.4.2.37: सीता'),
	]

