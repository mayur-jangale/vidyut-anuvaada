# Sutra प.4.2.64: प्रोक्ताल्लुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — proktAlluk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.64"
SUTRA_TEXT = "प्रोक्ताल्लुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — proktAlluk"


class Sutra4264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.64: अग्निः'),
		('रामः', '', 'प.4.2.64: रामः'),
		('सीता', '', 'प.4.2.64: सीता'),
	]

