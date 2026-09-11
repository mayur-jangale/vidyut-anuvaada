# Sutra प.4.4.22: संसृष्टे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMsfzwe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.22"
SUTRA_TEXT = "संसृष्टे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMsfzwe"


class Sutra4422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.22: अग्निः'),
		('रामः', '', 'प.4.4.22: रामः'),
		('सीता', '', 'प.4.4.22: सीता'),
	]

