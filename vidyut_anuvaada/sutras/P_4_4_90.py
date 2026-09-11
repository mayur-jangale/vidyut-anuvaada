# Sutra प.4.4.90: गृहपतिना संयुक्ते ञ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gfhapatinA saMyukte YyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.90"
SUTRA_TEXT = "गृहपतिना संयुक्ते ञ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gfhapatinA saMyukte YyaH"


class Sutra4490:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.90: अग्निः'),
		('रामः', '', 'प.4.4.90: रामः'),
		('सीता', '', 'प.4.4.90: सीता'),
	]

