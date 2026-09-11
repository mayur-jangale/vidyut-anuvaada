# Sutra प.4.3.121: रथाद्यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — raTAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.121"
SUTRA_TEXT = "रथाद्यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — raTAdyat"


class Sutra43121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.121: अग्निः'),
		('रामः', '', 'प.4.3.121: रामः'),
		('सीता', '', 'प.4.3.121: सीता'),
	]

