# Sutra प.4.4.137: सोममर्हति यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — somamarhati yaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.137"
SUTRA_TEXT = "सोममर्हति यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — somamarhati yaH"


class Sutra44137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.137: अग्निः'),
		('रामः', '', 'प.4.4.137: रामः'),
		('सीता', '', 'प.4.4.137: सीता'),
	]

