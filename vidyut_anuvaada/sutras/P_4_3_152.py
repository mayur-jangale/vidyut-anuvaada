# Sutra प.4.3.152: तालादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tAlAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.152"
SUTRA_TEXT = "तालादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tAlAdiByo'R"


class Sutra43152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.152: अग्निः'),
		('रामः', '', 'प.4.3.152: रामः'),
		('सीता', '', 'प.4.3.152: सीता'),
	]

