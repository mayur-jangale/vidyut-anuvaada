# Sutra प.4.3.138: त्रपुजतुनोः षुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — trapujatunoH zuk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.138"
SUTRA_TEXT = "त्रपुजतुनोः षुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — trapujatunoH zuk"


class Sutra43138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.138: अग्निः'),
		('रामः', '', 'प.4.3.138: रामः'),
		('सीता', '', 'प.4.3.138: सीता'),
	]

