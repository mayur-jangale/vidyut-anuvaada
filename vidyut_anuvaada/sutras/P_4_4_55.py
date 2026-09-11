# Sutra प.4.4.55: शिल्पम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Silpam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.55"
SUTRA_TEXT = "शिल्पम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Silpam"


class Sutra4455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.55: अग्निः'),
		('रामः', '', 'प.4.4.55: रामः'),
		('सीता', '', 'प.4.4.55: सीता'),
	]

