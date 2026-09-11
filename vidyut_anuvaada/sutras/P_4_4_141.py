# Sutra प.4.4.141: नक्षत्राद्घः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatrAdGaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.141"
SUTRA_TEXT = "नक्षत्राद्घः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatrAdGaH"


class Sutra44141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.141: अग्निः'),
		('रामः', '', 'प.4.4.141: रामः'),
		('सीता', '', 'प.4.4.141: सीता'),
	]

