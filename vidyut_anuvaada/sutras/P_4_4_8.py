# Sutra प.4.4.8: चरति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — carati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.8"
SUTRA_TEXT = "चरति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — carati"


class Sutra448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.8: अग्निः'),
		('रामः', '', 'प.4.4.8: रामः'),
		('सीता', '', 'प.4.4.8: सीता'),
	]

