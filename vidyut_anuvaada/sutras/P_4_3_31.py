# Sutra प.4.3.31: अ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — a ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.31"
SUTRA_TEXT = "अ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — a ca"


class Sutra4331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.31: अग्निः'),
		('रामः', '', 'प.4.3.31: रामः'),
		('सीता', '', 'प.4.3.31: सीता'),
	]

