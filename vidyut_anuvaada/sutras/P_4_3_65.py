# Sutra प.4.3.65: कर्णललाटात् कनलंकारे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — karRalalAwAt kanalaMkAre

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.65"
SUTRA_TEXT = "कर्णललाटात् कनलंकारे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — karRalalAwAt kanalaMkAre"


class Sutra4365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.65: अग्निः'),
		('रामः', '', 'प.4.3.65: रामः'),
		('सीता', '', 'प.4.3.65: सीता'),
	]

