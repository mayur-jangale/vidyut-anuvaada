# Sutra प.4.4.102: कथादिभ्यष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kaTAdiByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.102"
SUTRA_TEXT = "कथादिभ्यष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kaTAdiByazWak"


class Sutra44102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.102: अग्निः'),
		('रामः', '', 'प.4.4.102: रामः'),
		('सीता', '', 'प.4.4.102: सीता'),
	]

