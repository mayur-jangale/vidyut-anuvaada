# Sutra प.4.4.136: मतौ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — matO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.136"
SUTRA_TEXT = "मतौ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — matO ca"


class Sutra44136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.136: अग्निः'),
		('रामः', '', 'प.4.4.136: रामः'),
		('सीता', '', 'प.4.4.136: सीता'),
	]

