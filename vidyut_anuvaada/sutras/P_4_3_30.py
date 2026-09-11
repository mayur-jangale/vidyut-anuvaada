# Sutra प.4.3.30: अमावास्याया वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — amAvAsyAyA vA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.30"
SUTRA_TEXT = "अमावास्याया वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — amAvAsyAyA vA"


class Sutra4330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.30: अग्निः'),
		('रामः', '', 'प.4.3.30: रामः'),
		('सीता', '', 'प.4.3.30: सीता'),
	]

