# Sutra प.4.2.108: मद्रेभ्योऽञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — madreByo'Y

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.108"
SUTRA_TEXT = "मद्रेभ्योऽञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — madreByo'Y"


class Sutra42108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.108: अग्निः'),
		('रामः', '', 'प.4.2.108: रामः'),
		('सीता', '', 'प.4.2.108: सीता'),
	]

