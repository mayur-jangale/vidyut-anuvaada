# Sutra प.4.3.85: तद्गच्छति पथिदूतयोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadgacCati paTidUtayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.85"
SUTRA_TEXT = "तद्गच्छति पथिदूतयोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadgacCati paTidUtayoH"


class Sutra4385:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.85: अग्निः'),
		('रामः', '', 'प.4.3.85: रामः'),
		('सीता', '', 'प.4.3.85: सीता'),
	]

