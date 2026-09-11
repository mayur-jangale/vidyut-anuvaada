# Sutra प.4.3.165: जम्ब्वा वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — jambvA vA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.165"
SUTRA_TEXT = "जम्ब्वा वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — jambvA vA"


class Sutra43165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.165: अग्निः'),
		('रामः', '', 'प.4.3.165: रामः'),
		('सीता', '', 'प.4.3.165: सीता'),
	]

