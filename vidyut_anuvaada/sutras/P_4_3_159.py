# Sutra प.4.3.159: एण्या ढञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — eRyA QaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.159"
SUTRA_TEXT = "एण्या ढञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — eRyA QaY"


class Sutra43159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.159: अग्निः'),
		('रामः', '', 'प.4.3.159: रामः'),
		('सीता', '', 'प.4.3.159: सीता'),
	]

