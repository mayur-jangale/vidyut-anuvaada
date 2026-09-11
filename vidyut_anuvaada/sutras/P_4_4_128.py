# Sutra प.4.4.128: मत्वर्थे मासतन्वोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — matvarTe mAsatanvoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.128"
SUTRA_TEXT = "मत्वर्थे मासतन्वोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — matvarTe mAsatanvoH"


class Sutra44128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.128: अग्निः'),
		('रामः', '', 'प.4.4.128: रामः'),
		('सीता', '', 'प.4.4.128: सीता'),
	]

