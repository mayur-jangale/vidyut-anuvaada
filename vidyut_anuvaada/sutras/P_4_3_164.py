# Sutra प.4.3.164: प्लक्षादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — plakzAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.164"
SUTRA_TEXT = "प्लक्षादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — plakzAdiByo'R"


class Sutra43164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.164: अग्निः'),
		('रामः', '', 'प.4.3.164: रामः'),
		('सीता', '', 'प.4.3.164: सीता'),
	]

