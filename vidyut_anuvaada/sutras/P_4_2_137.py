# Sutra प.4.2.137: गर्तोत्तरपदाच्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gartottarapadAcCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.137"
SUTRA_TEXT = "गर्तोत्तरपदाच्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gartottarapadAcCaH"


class Sutra42137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.137: अग्निः'),
		('रामः', '', 'प.4.2.137: रामः'),
		('सीता', '', 'प.4.2.137: सीता'),
	]

