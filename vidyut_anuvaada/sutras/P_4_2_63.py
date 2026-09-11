# Sutra प.4.2.63: वसन्तादिभ्यष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vasantAdiByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.63"
SUTRA_TEXT = "वसन्तादिभ्यष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vasantAdiByazWak"


class Sutra4263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.63: अग्निः'),
		('रामः', '', 'प.4.2.63: रामः'),
		('सीता', '', 'प.4.2.63: सीता'),
	]

