# Sutra प.4.3.146: पिष्टाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pizwAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.146"
SUTRA_TEXT = "पिष्टाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pizwAcca"


class Sutra43146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.146: अग्निः'),
		('रामः', '', 'प.4.3.146: रामः'),
		('सीता', '', 'प.4.3.146: सीता'),
	]

