# Sutra प.4.3.21: हेमन्ताच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — hemantAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.21"
SUTRA_TEXT = "हेमन्ताच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — hemantAcca"


class Sutra4321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.21: अग्निः'),
		('रामः', '', 'प.4.3.21: रामः'),
		('सीता', '', 'प.4.3.21: सीता'),
	]

