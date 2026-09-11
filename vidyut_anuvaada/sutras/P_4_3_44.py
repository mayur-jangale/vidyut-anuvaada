# Sutra प.4.3.44: उप्ते च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — upte ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.44"
SUTRA_TEXT = "उप्ते च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — upte ca"


class Sutra4344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.44: अग्निः'),
		('रामः', '', 'प.4.3.44: रामः'),
		('सीता', '', 'प.4.3.44: सीता'),
	]

