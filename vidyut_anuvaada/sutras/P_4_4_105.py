# Sutra प.4.4.105: सभाया यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saBAyA yaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.105"
SUTRA_TEXT = "सभाया यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saBAyA yaH"


class Sutra44105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.105: अग्निः'),
		('रामः', '', 'प.4.4.105: रामः'),
		('सीता', '', 'प.4.4.105: सीता'),
	]

