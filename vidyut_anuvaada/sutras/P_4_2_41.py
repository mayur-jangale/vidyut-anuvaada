# Sutra प.4.2.41: ठञ् कवचिनश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — WaY kavacinaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.41"
SUTRA_TEXT = "ठञ् कवचिनश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — WaY kavacinaSca"


class Sutra4241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.41: अग्निः'),
		('रामः', '', 'प.4.2.41: रामः'),
		('सीता', '', 'प.4.2.41: सीता'),
	]

