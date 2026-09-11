# Sutra प.4.3.74: तत आगतः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tata AgataH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.74"
SUTRA_TEXT = "तत आगतः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tata AgataH"


class Sutra4374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.74: अग्निः'),
		('रामः', '', 'प.4.3.74: रामः'),
		('सीता', '', 'प.4.3.74: सीता'),
	]

