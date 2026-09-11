# Sutra प.4.2.20: क्षीराड्ढञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kzIrAqQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.20"
SUTRA_TEXT = "क्षीराड्ढञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kzIrAqQaY"


class Sutra4220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.20: अग्निः'),
		('रामः', '', 'प.4.2.20: रामः'),
		('सीता', '', 'प.4.2.20: सीता'),
	]

