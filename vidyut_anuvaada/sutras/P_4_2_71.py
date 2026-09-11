# Sutra प.4.2.71: ओरञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — oraY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.71"
SUTRA_TEXT = "ओरञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — oraY"


class Sutra4271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.71: अग्निः'),
		('रामः', '', 'प.4.2.71: रामः'),
		('सीता', '', 'प.4.2.71: सीता'),
	]

