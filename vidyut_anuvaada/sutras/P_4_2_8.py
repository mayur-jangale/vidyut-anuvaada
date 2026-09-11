# Sutra प.4.2.8: कलेर्ढक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kalerQak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.8"
SUTRA_TEXT = "कलेर्ढक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kalerQak"


class Sutra428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.8: अग्निः'),
		('रामः', '', 'प.4.2.8: रामः'),
		('सीता', '', 'प.4.2.8: सीता'),
	]

