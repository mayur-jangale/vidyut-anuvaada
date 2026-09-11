# Sutra प.4.4.1: प्राग्वहतेष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prAgvahatezWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.1"
SUTRA_TEXT = "प्राग्वहतेष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prAgvahatezWak"


class Sutra441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.1: अग्निः'),
		('रामः', '', 'प.4.4.1: रामः'),
		('सीता', '', 'प.4.4.1: सीता'),
	]

