# Sutra प.4.2.38: भिक्षादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BikzAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.38"
SUTRA_TEXT = "भिक्षादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BikzAdiByo'R"


class Sutra4238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.38: अग्निः'),
		('रामः', '', 'प.4.2.38: रामः'),
		('सीता', '', 'प.4.2.38: सीता'),
	]

