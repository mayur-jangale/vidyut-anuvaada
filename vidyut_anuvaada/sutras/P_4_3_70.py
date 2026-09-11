# Sutra प.4.3.70: पौरोडाशपुरोडाशात् ष्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pOroqASapuroqASAt zWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.70"
SUTRA_TEXT = "पौरोडाशपुरोडाशात् ष्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pOroqASapuroqASAt zWan"


class Sutra4370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.70: अग्निः'),
		('रामः', '', 'प.4.3.70: रामः'),
		('सीता', '', 'प.4.3.70: सीता'),
	]

