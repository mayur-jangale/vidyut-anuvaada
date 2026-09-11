# Sutra प.4.3.54: दिगादिभ्यो यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — digAdiByo yat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.54"
SUTRA_TEXT = "दिगादिभ्यो यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — digAdiByo yat"


class Sutra4354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.54: अग्निः'),
		('रामः', '', 'प.4.3.54: रामः'),
		('सीता', '', 'प.4.3.54: सीता'),
	]

