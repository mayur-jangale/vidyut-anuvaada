# Sutra प.4.4.101: परिषदो ण्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parizado RyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.101"
SUTRA_TEXT = "परिषदो ण्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parizado RyaH"


class Sutra44101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.101: अग्निः'),
		('रामः', '', 'प.4.4.101: रामः'),
		('सीता', '', 'प.4.4.101: सीता'),
	]

