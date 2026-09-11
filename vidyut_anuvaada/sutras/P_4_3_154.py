# Sutra प.4.3.154: प्राणिरजतादिभ्योऽञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prARirajatAdiByo'Y

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.154"
SUTRA_TEXT = "प्राणिरजतादिभ्योऽञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prARirajatAdiByo'Y"


class Sutra43154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.154: अग्निः'),
		('रामः', '', 'प.4.3.154: रामः'),
		('सीता', '', 'प.4.3.154: सीता'),
	]

