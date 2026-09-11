# Sutra प.4.4.139: मधोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maDoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.139"
SUTRA_TEXT = "मधोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maDoH"


class Sutra44139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.139: अग्निः'),
		('रामः', '', 'प.4.4.139: रामः'),
		('सीता', '', 'प.4.4.139: सीता'),
	]

