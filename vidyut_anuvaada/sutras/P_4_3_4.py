# Sutra प.4.3.4: अर्धाद्यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — arDAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.4"
SUTRA_TEXT = "अर्धाद्यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — arDAdyat"


class Sutra434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.4: अग्निः'),
		('रामः', '', 'प.4.3.4: रामः'),
		('सीता', '', 'प.4.3.4: सीता'),
	]

