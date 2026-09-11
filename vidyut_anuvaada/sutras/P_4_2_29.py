# Sutra प.4.2.29: महेन्द्राद्घाणौ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mahendrAdGARO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.29"
SUTRA_TEXT = "महेन्द्राद्घाणौ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mahendrAdGARO ca"


class Sutra4229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.29: अग्निः'),
		('रामः', '', 'प.4.2.29: रामः'),
		('सीता', '', 'प.4.2.29: सीता'),
	]

