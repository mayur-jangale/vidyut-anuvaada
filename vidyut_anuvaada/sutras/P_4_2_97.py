# Sutra प.4.2.97: नद्यादिभ्यो ढक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nadyAdiByo Qak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.97"
SUTRA_TEXT = "नद्यादिभ्यो ढक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nadyAdiByo Qak"


class Sutra4297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.97: अग्निः'),
		('रामः', '', 'प.4.2.97: रामः'),
		('सीता', '', 'प.4.2.97: सीता'),
	]

