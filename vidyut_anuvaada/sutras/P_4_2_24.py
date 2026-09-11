# Sutra प.4.2.24: सास्य देवता
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sAsya devatA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.24"
SUTRA_TEXT = "सास्य देवता"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sAsya devatA"


class Sutra4224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.24: अग्निः'),
		('रामः', '', 'प.4.2.24: रामः'),
		('सीता', '', 'प.4.2.24: सीता'),
	]

