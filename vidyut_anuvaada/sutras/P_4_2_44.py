# Sutra प.4.2.44: अनुदात्तादेरञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — anudAttAderaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.44"
SUTRA_TEXT = "अनुदात्तादेरञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — anudAttAderaY"


class Sutra4244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.44: अग्निः'),
		('रामः', '', 'प.4.2.44: रामः'),
		('सीता', '', 'प.4.2.44: सीता'),
	]

