# Sutra प.4.3.96: अचित्ताददेशकालाट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — acittAdadeSakAlAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.96"
SUTRA_TEXT = "अचित्ताददेशकालाट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — acittAdadeSakAlAwWak"


class Sutra4396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.96: अग्निः'),
		('रामः', '', 'प.4.3.96: रामः'),
		('सीता', '', 'प.4.3.96: सीता'),
	]

