# Sutra प.4.2.7: दृष्टं साम
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dfzwaM sAma

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.7"
SUTRA_TEXT = "दृष्टं साम"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dfzwaM sAma"


class Sutra427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.7: अग्निः'),
		('रामः', '', 'प.4.2.7: रामः'),
		('सीता', '', 'प.4.2.7: सीता'),
	]

