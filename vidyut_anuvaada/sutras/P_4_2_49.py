# Sutra प.4.2.49: पाशादिभ्यो यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pASAdiByo yaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.49"
SUTRA_TEXT = "पाशादिभ्यो यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pASAdiByo yaH"


class Sutra4249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.49: अग्निः'),
		('रामः', '', 'प.4.2.49: रामः'),
		('सीता', '', 'प.4.2.49: सीता'),
	]

