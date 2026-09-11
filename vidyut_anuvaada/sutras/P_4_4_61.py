# Sutra प.4.4.61: शीलम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SIlam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.61"
SUTRA_TEXT = "शीलम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SIlam"


class Sutra4461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.61: अग्निः'),
		('रामः', '', 'प.4.4.61: रामः'),
		('सीता', '', 'प.4.4.61: सीता'),
	]

