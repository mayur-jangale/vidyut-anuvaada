# Sutra प.4.2.74: उदक् च विपाशः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — udak ca vipASaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.74"
SUTRA_TEXT = "उदक् च विपाशः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — udak ca vipASaH"


class Sutra4274:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.74: अग्निः'),
		('रामः', '', 'प.4.2.74: रामः'),
		('सीता', '', 'प.4.2.74: सीता'),
	]

