# Sutra प.4.3.136: बिल्वादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — bilvAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.136"
SUTRA_TEXT = "बिल्वादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — bilvAdiByo'R"


class Sutra43136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.136: अग्निः'),
		('रामः', '', 'प.4.3.136: रामः'),
		('सीता', '', 'प.4.3.136: सीता'),
	]

