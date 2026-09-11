# Sutra प.4.4.43: समवायान् समवैति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — samavAyAn samavEti

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.43"
SUTRA_TEXT = "समवायान् समवैति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — samavAyAn samavEti"


class Sutra4443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.43: अग्निः'),
		('रामः', '', 'प.4.4.43: रामः'),
		('सीता', '', 'प.4.4.43: सीता'),
	]

