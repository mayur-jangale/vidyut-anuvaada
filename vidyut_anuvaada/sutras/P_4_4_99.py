# Sutra प.4.4.99: प्रतिजनादिभ्यः खञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pratijanAdiByaH KaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.99"
SUTRA_TEXT = "प्रतिजनादिभ्यः खञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pratijanAdiByaH KaY"


class Sutra4499:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.99: अग्निः'),
		('रामः', '', 'प.4.4.99: रामः'),
		('सीता', '', 'प.4.4.99: सीता'),
	]

