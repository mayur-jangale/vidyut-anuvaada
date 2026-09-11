# Sutra प.4.3.25: तत्र जातः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tatra jAtaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.25"
SUTRA_TEXT = "तत्र जातः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tatra jAtaH"


class Sutra4325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.25: अग्निः'),
		('रामः', '', 'प.4.3.25: रामः'),
		('सीता', '', 'प.4.3.25: सीता'),
	]

