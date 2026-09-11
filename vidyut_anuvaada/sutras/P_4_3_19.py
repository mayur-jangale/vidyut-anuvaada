# Sutra प.4.3.19: छन्दसि ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Candasi WaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.19"
SUTRA_TEXT = "छन्दसि ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Candasi WaY"


class Sutra4319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.19: अग्निः'),
		('रामः', '', 'प.4.3.19: रामः'),
		('सीता', '', 'प.4.3.19: सीता'),
	]

