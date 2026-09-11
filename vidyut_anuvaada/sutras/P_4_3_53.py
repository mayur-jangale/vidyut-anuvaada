# Sutra प.4.3.53: तत्र भवः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tatra BavaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.53"
SUTRA_TEXT = "तत्र भवः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tatra BavaH"


class Sutra4353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.53: अग्निः'),
		('रामः', '', 'प.4.3.53: रामः'),
		('सीता', '', 'प.4.3.53: सीता'),
	]

