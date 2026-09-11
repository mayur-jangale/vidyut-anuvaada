# Sutra प.4.4.110: भवे छन्दसि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Bave Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.110"
SUTRA_TEXT = "भवे छन्दसि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Bave Candasi"


class Sutra44110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.110: अग्निः'),
		('रामः', '', 'प.4.4.110: रामः'),
		('सीता', '', 'प.4.4.110: सीता'),
	]

