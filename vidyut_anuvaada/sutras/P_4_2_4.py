# Sutra प.4.2.4: लुबविशेषे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — lubaviSeze

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.4"
SUTRA_TEXT = "लुबविशेषे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — lubaviSeze"


class Sutra424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.4: अग्निः'),
		('रामः', '', 'प.4.2.4: रामः'),
		('सीता', '', 'प.4.2.4: सीता'),
	]

