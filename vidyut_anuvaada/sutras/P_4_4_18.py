# Sutra प.4.4.18: अण् कुटिलिकायाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aR kuwilikAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.18"
SUTRA_TEXT = "अण् कुटिलिकायाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aR kuwilikAyAH"


class Sutra4418:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.18: अग्निः'),
		('रामः', '', 'प.4.4.18: रामः'),
		('सीता', '', 'प.4.4.18: सीता'),
	]

