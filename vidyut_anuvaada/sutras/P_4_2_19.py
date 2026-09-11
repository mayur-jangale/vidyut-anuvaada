# Sutra प.4.2.19: उदश्वितोऽन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — udaSvito'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.19"
SUTRA_TEXT = "उदश्वितोऽन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — udaSvito'nyatarasyAm"


class Sutra4219:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.19: अग्निः'),
		('रामः', '', 'प.4.2.19: रामः'),
		('सीता', '', 'प.4.2.19: सीता'),
	]

