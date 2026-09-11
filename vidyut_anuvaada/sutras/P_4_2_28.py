# Sutra प.4.2.28: छ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Ca ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.28"
SUTRA_TEXT = "छ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Ca ca"


class Sutra4228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.28: अग्निः'),
		('रामः', '', 'प.4.2.28: रामः'),
		('सीता', '', 'प.4.2.28: सीता'),
	]

