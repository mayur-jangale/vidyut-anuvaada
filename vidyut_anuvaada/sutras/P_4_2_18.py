# Sutra प.4.2.18: दध्नष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — daDnazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.18"
SUTRA_TEXT = "दध्नष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — daDnazWak"


class Sutra4218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.18: अग्निः'),
		('रामः', '', 'प.4.2.18: रामः'),
		('सीता', '', 'प.4.2.18: सीता'),
	]

