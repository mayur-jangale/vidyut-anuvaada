# Sutra प.4.4.26: व्यञ्जनैरुपसिक्ते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vyaYjanErupasikte

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.26"
SUTRA_TEXT = "व्यञ्जनैरुपसिक्ते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vyaYjanErupasikte"


class Sutra4426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.26: अग्निः'),
		('रामः', '', 'प.4.4.26: रामः'),
		('सीता', '', 'प.4.4.26: सीता'),
	]

