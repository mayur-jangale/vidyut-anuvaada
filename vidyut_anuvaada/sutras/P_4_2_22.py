# Sutra प.4.2.22: आग्रहायण्यश्वत्थाट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AgrahAyaRyaSvatTAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.22"
SUTRA_TEXT = "आग्रहायण्यश्वत्थाट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AgrahAyaRyaSvatTAwWak"


class Sutra4222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.22: अग्निः'),
		('रामः', '', 'प.4.2.22: रामः'),
		('सीता', '', 'प.4.2.22: सीता'),
	]

