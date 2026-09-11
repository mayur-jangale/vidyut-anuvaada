# Sutra प.4.4.116: अग्राद्यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — agrAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.116"
SUTRA_TEXT = "अग्राद्यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — agrAdyat"


class Sutra44116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.116: अग्निः'),
		('रामः', '', 'प.4.4.116: रामः'),
		('सीता', '', 'प.4.4.116: सीता'),
	]

