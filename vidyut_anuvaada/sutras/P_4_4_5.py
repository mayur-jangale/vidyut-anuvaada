# Sutra प.4.4.5: तरति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tarati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.5"
SUTRA_TEXT = "तरति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tarati"


class Sutra445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.5: अग्निः'),
		('रामः', '', 'प.4.4.5: रामः'),
		('सीता', '', 'प.4.4.5: सीता'),
	]

