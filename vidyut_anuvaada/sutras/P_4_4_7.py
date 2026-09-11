# Sutra प.4.4.7: नौद्व्यचष्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nOdvyacazWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.7"
SUTRA_TEXT = "नौद्व्यचष्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nOdvyacazWan"


class Sutra447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.7: अग्निः'),
		('रामः', '', 'प.4.4.7: रामः'),
		('सीता', '', 'प.4.4.7: सीता'),
	]

