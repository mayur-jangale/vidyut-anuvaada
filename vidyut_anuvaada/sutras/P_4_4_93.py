# Sutra प.4.4.93: छन्दसो निर्मिते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Candaso nirmite

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.93"
SUTRA_TEXT = "छन्दसो निर्मिते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Candaso nirmite"


class Sutra4493:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.93: अग्निः'),
		('रामः', '', 'प.4.4.93: रामः'),
		('सीता', '', 'प.4.4.93: सीता'),
	]

