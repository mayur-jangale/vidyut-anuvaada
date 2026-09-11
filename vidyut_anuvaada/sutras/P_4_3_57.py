# Sutra प.4.3.57: ग्रीवाभ्योऽण् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grIvAByo'R ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.57"
SUTRA_TEXT = "ग्रीवाभ्योऽण् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grIvAByo'R ca"


class Sutra4357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.57: अग्निः'),
		('रामः', '', 'प.4.3.57: रामः'),
		('सीता', '', 'प.4.3.57: सीता'),
	]

