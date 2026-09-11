# Sutra प.4.3.40: उपजानूपकर्णोपनीवेष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — upajAnUpakarRopanIvezWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.40"
SUTRA_TEXT = "उपजानूपकर्णोपनीवेष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — upajAnUpakarRopanIvezWak"


class Sutra4340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.40: अग्निः'),
		('रामः', '', 'प.4.3.40: रामः'),
		('सीता', '', 'प.4.3.40: सीता'),
	]

