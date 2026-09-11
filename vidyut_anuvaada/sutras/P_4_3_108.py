# Sutra प.4.3.108: कलापिनोऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kalApino'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.108"
SUTRA_TEXT = "कलापिनोऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kalApino'R"


class Sutra43108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.108: अग्निः'),
		('रामः', '', 'प.4.3.108: रामः'),
		('सीता', '', 'प.4.3.108: सीता'),
	]

