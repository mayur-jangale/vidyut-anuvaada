# Sutra प.4.4.58: परश्वधाट्ठञ्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — paraSvaDAwWaYca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.58"
SUTRA_TEXT = "परश्वधाट्ठञ्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — paraSvaDAwWaYca"


class Sutra4458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.58: अग्निः'),
		('रामः', '', 'प.4.4.58: रामः'),
		('सीता', '', 'प.4.4.58: सीता'),
	]

