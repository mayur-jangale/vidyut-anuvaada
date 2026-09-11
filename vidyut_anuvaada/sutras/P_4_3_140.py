# Sutra प.4.3.140: अनुदात्तादेश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — anudAttAdeSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.140"
SUTRA_TEXT = "अनुदात्तादेश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — anudAttAdeSca"


class Sutra43140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.140: अग्निः'),
		('रामः', '', 'प.4.3.140: रामः'),
		('सीता', '', 'प.4.3.140: सीता'),
	]

