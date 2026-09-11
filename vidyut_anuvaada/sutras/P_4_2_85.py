# Sutra प.4.2.85: नद्यां मतुप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nadyAM matup

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.85"
SUTRA_TEXT = "नद्यां मतुप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nadyAM matup"


class Sutra4285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.85: अग्निः'),
		('रामः', '', 'प.4.2.85: रामः'),
		('सीता', '', 'प.4.2.85: सीता'),
	]

