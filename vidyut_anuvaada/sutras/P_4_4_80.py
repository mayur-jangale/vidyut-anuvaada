# Sutra प.4.4.80: शकटादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SakawAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.80"
SUTRA_TEXT = "शकटादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SakawAdaR"


class Sutra4480:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.80: अग्निः'),
		('रामः', '', 'प.4.4.80: रामः'),
		('सीता', '', 'प.4.4.80: सीता'),
	]

