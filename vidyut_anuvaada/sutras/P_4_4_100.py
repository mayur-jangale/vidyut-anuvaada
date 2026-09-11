# Sutra प.4.4.100: भक्ताण्णः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BaktARRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.100"
SUTRA_TEXT = "भक्ताण्णः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BaktARRaH"


class Sutra44100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.100: अग्निः'),
		('रामः', '', 'प.4.4.100: रामः'),
		('सीता', '', 'प.4.4.100: सीता'),
	]

