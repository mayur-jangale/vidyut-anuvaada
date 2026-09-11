# Sutra प.4.3.141: पलाशादिभ्यो वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — palASAdiByo vA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.141"
SUTRA_TEXT = "पलाशादिभ्यो वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — palASAdiByo vA"


class Sutra43141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.141: अग्निः'),
		('रामः', '', 'प.4.3.141: रामः'),
		('सीता', '', 'प.4.3.141: सीता'),
	]

