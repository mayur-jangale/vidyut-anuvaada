# Sutra प.4.2.123: रोपधेतोः प्राचाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ropaDetoH prAcAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.123"
SUTRA_TEXT = "रोपधेतोः प्राचाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ropaDetoH prAcAm"


class Sutra42123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.123: अग्निः'),
		('रामः', '', 'प.4.2.123: रामः'),
		('सीता', '', 'प.4.2.123: सीता'),
	]

