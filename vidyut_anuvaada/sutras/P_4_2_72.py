# Sutra प.4.2.72: मतोश्च बह्वजङ्गात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — matoSca bahvajaNgAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.72"
SUTRA_TEXT = "मतोश्च बह्वजङ्गात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — matoSca bahvajaNgAt"


class Sutra4272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.72: अग्निः'),
		('रामः', '', 'प.4.2.72: रामः'),
		('सीता', '', 'प.4.2.72: सीता'),
	]

