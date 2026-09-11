# Sutra प.4.2.25: कस्येत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kasyet

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.25"
SUTRA_TEXT = "कस्येत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kasyet"


class Sutra4225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.25: अग्निः'),
		('रामः', '', 'प.4.2.25: रामः'),
		('सीता', '', 'प.4.2.25: सीता'),
	]

