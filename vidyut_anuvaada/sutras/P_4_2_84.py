# Sutra प.4.2.84: ठक्छौ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — WakCO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.84"
SUTRA_TEXT = "ठक्छौ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — WakCO ca"


class Sutra4284:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.84: अग्निः'),
		('रामः', '', 'प.4.2.84: रामः'),
		('सीता', '', 'प.4.2.84: सीता'),
	]

