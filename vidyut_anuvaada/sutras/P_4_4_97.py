# Sutra प.4.4.97: मतजनहलात् करणजल्पकर्षेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — matajanahalAt karaRajalpakarzezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.97"
SUTRA_TEXT = "मतजनहलात् करणजल्पकर्षेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — matajanahalAt karaRajalpakarzezu"


class Sutra4497:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.97: अग्निः'),
		('रामः', '', 'प.4.4.97: रामः'),
		('सीता', '', 'प.4.4.97: सीता'),
	]

