# Sutra प.4.4.19: निर्वृत्तेऽक्षद्यूतादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nirvftte'kzadyUtAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.19"
SUTRA_TEXT = "निर्वृत्तेऽक्षद्यूतादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nirvftte'kzadyUtAdiByaH"


class Sutra4419:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.19: अग्निः'),
		('रामः', '', 'प.4.4.19: रामः'),
		('सीता', '', 'प.4.4.19: सीता'),
	]

