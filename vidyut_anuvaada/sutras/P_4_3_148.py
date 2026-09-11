# Sutra प.4.3.148: व्रीहेः पुरोडाशे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vrIheH puroqASe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.148"
SUTRA_TEXT = "व्रीहेः पुरोडाशे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vrIheH puroqASe"


class Sutra43148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.148: अग्निः'),
		('रामः', '', 'प.4.3.148: रामः'),
		('सीता', '', 'प.4.3.148: सीता'),
	]

