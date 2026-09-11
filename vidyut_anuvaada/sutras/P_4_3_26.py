# Sutra प.4.3.26: प्रावृषष्ठप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prAvfzazWap

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.26"
SUTRA_TEXT = "प्रावृषष्ठप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prAvfzazWap"


class Sutra4326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.26: अग्निः'),
		('रामः', '', 'प.4.3.26: रामः'),
		('सीता', '', 'प.4.3.26: सीता'),
	]

