# Sutra प.4.3.1: युष्मदस्मदोरन्यतरस्यां खञ् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — yuzmadasmadoranyatarasyAM KaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.1"
SUTRA_TEXT = "युष्मदस्मदोरन्यतरस्यां खञ् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — yuzmadasmadoranyatarasyAM KaY ca"


class Sutra431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.1: अग्निः'),
		('रामः', '', 'प.4.3.1: रामः'),
		('सीता', '', 'प.4.3.1: सीता'),
	]

