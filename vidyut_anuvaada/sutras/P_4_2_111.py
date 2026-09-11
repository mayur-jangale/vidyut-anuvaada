# Sutra प.4.2.111: कण्वादिभ्यो गोत्रे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kaRvAdiByo gotre

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.111"
SUTRA_TEXT = "कण्वादिभ्यो गोत्रे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kaRvAdiByo gotre"


class Sutra42111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.111: अग्निः'),
		('रामः', '', 'प.4.2.111: रामः'),
		('सीता', '', 'प.4.2.111: सीता'),
	]

