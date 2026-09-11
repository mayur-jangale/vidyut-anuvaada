# Sutra प.4.3.134: तस्य विकारः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasya vikAraH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.134"
SUTRA_TEXT = "तस्य विकारः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasya vikAraH"


class Sutra43134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.134: अग्निः'),
		('रामः', '', 'प.4.3.134: रामः'),
		('सीता', '', 'प.4.3.134: सीता'),
	]

