# Sutra प.4.2.10: परिवृतो रथः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parivfto raTaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.10"
SUTRA_TEXT = "परिवृतो रथः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parivfto raTaH"


class Sutra4210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.10: अग्निः'),
		('रामः', '', 'प.4.2.10: रामः'),
		('सीता', '', 'प.4.2.10: सीता'),
	]

