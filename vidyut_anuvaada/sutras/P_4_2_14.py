# Sutra प.4.2.14: तत्रोद्धृतममत्रेभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tatrodDftamamatreByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.14"
SUTRA_TEXT = "तत्रोद्धृतममत्रेभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tatrodDftamamatreByaH"


class Sutra4214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.14: अग्निः'),
		('रामः', '', 'प.4.2.14: रामः'),
		('सीता', '', 'प.4.2.14: सीता'),
	]

