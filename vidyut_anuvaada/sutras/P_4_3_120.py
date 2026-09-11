# Sutra प.4.3.120: तस्येदम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasyedam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.120"
SUTRA_TEXT = "तस्येदम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasyedam"


class Sutra43120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.120: अग्निः'),
		('रामः', '', 'प.4.3.120: रामः'),
		('सीता', '', 'प.4.3.120: सीता'),
	]

