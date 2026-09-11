# Sutra प.4.4.133: पूर्वैः कृतमिनयौ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pUrvEH kftaminayO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.133"
SUTRA_TEXT = "पूर्वैः कृतमिनयौ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pUrvEH kftaminayO ca"


class Sutra44133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.133: अग्निः'),
		('रामः', '', 'प.4.4.133: रामः'),
		('सीता', '', 'प.4.4.133: सीता'),
	]

