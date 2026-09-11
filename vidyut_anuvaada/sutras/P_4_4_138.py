# Sutra प.4.4.138: मये च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maye ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.138"
SUTRA_TEXT = "मये च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maye ca"


class Sutra44138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.138: अग्निः'),
		('रामः', '', 'प.4.4.138: रामः'),
		('सीता', '', 'प.4.4.138: सीता'),
	]

