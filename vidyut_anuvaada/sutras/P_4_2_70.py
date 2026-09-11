# Sutra प.4.2.70: अदूरभवश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — adUraBavaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.70"
SUTRA_TEXT = "अदूरभवश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — adUraBavaSca"


class Sutra4270:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.70: अग्निः'),
		('रामः', '', 'प.4.2.70: रामः'),
		('सीता', '', 'प.4.2.70: सीता'),
	]

