# Sutra प.4.3.139: ओरञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — oraY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.139"
SUTRA_TEXT = "ओरञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — oraY"


class Sutra43139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.139: अग्निः'),
		('रामः', '', 'प.4.3.139: रामः'),
		('सीता', '', 'प.4.3.139: सीता'),
	]

