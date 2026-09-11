# Sutra प.4.4.98: तत्र साधुः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tatra sADuH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.98"
SUTRA_TEXT = "तत्र साधुः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tatra sADuH"


class Sutra4498:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.98: अग्निः'),
		('रामः', '', 'प.4.4.98: रामः'),
		('सीता', '', 'प.4.4.98: सीता'),
	]

