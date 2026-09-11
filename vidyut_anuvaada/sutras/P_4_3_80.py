# Sutra प.4.3.80: गोत्रादङ्कवत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gotrAdaNkavat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.80"
SUTRA_TEXT = "गोत्रादङ्कवत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gotrAdaNkavat"


class Sutra4380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.80: अग्निः'),
		('रामः', '', 'प.4.3.80: रामः'),
		('सीता', '', 'प.4.3.80: सीता'),
	]

