# Sutra प.4.4.118: समुद्राभ्राद्घः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — samudrABrAdGaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.118"
SUTRA_TEXT = "समुद्राभ्राद्घः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — samudrABrAdGaH"


class Sutra44118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.118: अग्निः'),
		('रामः', '', 'प.4.4.118: रामः'),
		('सीता', '', 'प.4.4.118: सीता'),
	]

