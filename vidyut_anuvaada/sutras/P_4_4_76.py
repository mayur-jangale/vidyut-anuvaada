# Sutra प.4.4.76: तद्वहति रथयुगप्रासङ्गम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadvahati raTayugaprAsaNgam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.76"
SUTRA_TEXT = "तद्वहति रथयुगप्रासङ्गम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadvahati raTayugaprAsaNgam"


class Sutra4476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.76: अग्निः'),
		('रामः', '', 'प.4.4.76: रामः'),
		('सीता', '', 'प.4.4.76: सीता'),
	]

