# Sutra प.4.3.115: उपज्ञाते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — upajYAte

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.115"
SUTRA_TEXT = "उपज्ञाते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — upajYAte"


class Sutra43115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.115: अग्निः'),
		('रामः', '', 'प.4.3.115: रामः'),
		('सीता', '', 'प.4.3.115: सीता'),
	]

