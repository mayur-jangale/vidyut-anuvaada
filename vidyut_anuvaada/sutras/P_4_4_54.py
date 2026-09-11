# Sutra प.4.4.54: शलालुनोऽन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SalAluno'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.54"
SUTRA_TEXT = "शलालुनोऽन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SalAluno'nyatarasyAm"


class Sutra4454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.54: अग्निः'),
		('रामः', '', 'प.4.4.54: रामः'),
		('सीता', '', 'प.4.4.54: सीता'),
	]

