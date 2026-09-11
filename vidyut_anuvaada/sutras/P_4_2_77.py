# Sutra प.4.2.77: सुवास्त्वादिभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — suvAstvAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.77"
SUTRA_TEXT = "सुवास्त्वादिभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — suvAstvAdiByo'R"


class Sutra4277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.77: अग्निः'),
		('रामः', '', 'प.4.2.77: रामः'),
		('सीता', '', 'प.4.2.77: सीता'),
	]

