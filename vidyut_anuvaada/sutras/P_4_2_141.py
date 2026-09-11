# Sutra प.4.2.141: वृद्धादकेकान्तखोपधात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAdakekAntaKopaDAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.141"
SUTRA_TEXT = "वृद्धादकेकान्तखोपधात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAdakekAntaKopaDAt"


class Sutra42141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.141: अग्निः'),
		('रामः', '', 'प.4.2.141: रामः'),
		('सीता', '', 'प.4.2.141: सीता'),
	]

