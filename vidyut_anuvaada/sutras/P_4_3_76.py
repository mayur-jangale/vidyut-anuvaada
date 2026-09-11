# Sutra प.4.3.76: शुण्डिकादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SuRqikAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.76"
SUTRA_TEXT = "शुण्डिकादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SuRqikAdiByo'R"


class Sutra4376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.76: अग्निः'),
		('रामः', '', 'प.4.3.76: रामः'),
		('सीता', '', 'प.4.3.76: सीता'),
	]

