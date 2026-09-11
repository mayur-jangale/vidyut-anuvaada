# Sutra प.4.3.118: कुलालादिभ्यो वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kulAlAdiByo vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.118"
SUTRA_TEXT = "कुलालादिभ्यो वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kulAlAdiByo vuY"


class Sutra43118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.118: अग्निः'),
		('रामः', '', 'प.4.3.118: रामः'),
		('सीता', '', 'प.4.3.118: सीता'),
	]

