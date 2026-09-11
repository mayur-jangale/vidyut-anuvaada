# Sutra प.4.2.13: कौमारापूर्ववचने
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kOmArApUrvavacane

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.13"
SUTRA_TEXT = "कौमारापूर्ववचने"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kOmArApUrvavacane"


class Sutra4213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.13: अग्निः'),
		('रामः', '', 'प.4.2.13: रामः'),
		('सीता', '', 'प.4.2.13: सीता'),
	]

