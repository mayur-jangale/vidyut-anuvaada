# Sutra प.4.3.90: अभिजनश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aBijanaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.90"
SUTRA_TEXT = "अभिजनश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aBijanaSca"


class Sutra4390:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.90: अग्निः'),
		('रामः', '', 'प.4.3.90: रामः'),
		('सीता', '', 'प.4.3.90: सीता'),
	]

