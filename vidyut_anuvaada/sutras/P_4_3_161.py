# Sutra प.4.3.161: द्रोश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — droSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.161"
SUTRA_TEXT = "द्रोश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — droSca"


class Sutra43161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.161: अग्निः'),
		('रामः', '', 'प.4.3.161: रामः'),
		('सीता', '', 'प.4.3.161: सीता'),
	]

