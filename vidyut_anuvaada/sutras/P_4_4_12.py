# Sutra प.4.4.12: वेतनादिभ्यो जीवति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vetanAdiByo jIvati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.12"
SUTRA_TEXT = "वेतनादिभ्यो जीवति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vetanAdiByo jIvati"


class Sutra4412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.12: अग्निः'),
		('रामः', '', 'प.4.4.12: रामः'),
		('सीता', '', 'प.4.4.12: सीता'),
	]

