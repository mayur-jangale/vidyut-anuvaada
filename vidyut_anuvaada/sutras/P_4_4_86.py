# Sutra प.4.4.86: वशं गतः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vaSaM gataH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.86"
SUTRA_TEXT = "वशं गतः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vaSaM gataH"


class Sutra4486:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.86: अग्निः'),
		('रामः', '', 'प.4.4.86: रामः'),
		('सीता', '', 'प.4.4.86: सीता'),
	]

