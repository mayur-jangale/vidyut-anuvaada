# Sutra प.4.2.114: वृद्धाच्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAcCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.114"
SUTRA_TEXT = "वृद्धाच्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAcCaH"


class Sutra42114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.114: अग्निः'),
		('रामः', '', 'प.4.2.114: रामः'),
		('सीता', '', 'प.4.2.114: सीता'),
	]

