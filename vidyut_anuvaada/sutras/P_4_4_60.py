# Sutra प.4.4.60: अस्तिनास्तिदिष्टं मतिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — astinAstidizwaM matiH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.60"
SUTRA_TEXT = "अस्तिनास्तिदिष्टं मतिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — astinAstidizwaM matiH"


class Sutra4460:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.60: अग्निः'),
		('रामः', '', 'प.4.4.60: रामः'),
		('सीता', '', 'प.4.4.60: सीता'),
	]

