# Sutra प.4.4.94: उरसोऽण् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — uraso'R ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.94"
SUTRA_TEXT = "उरसोऽण् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — uraso'R ca"


class Sutra4494:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.94: अग्निः'),
		('रामः', '', 'प.4.4.94: रामः'),
		('सीता', '', 'प.4.4.94: सीता'),
	]

