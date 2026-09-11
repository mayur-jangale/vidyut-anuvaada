# Sutra प.4.2.78: रोणी
# (Sup-sthāna (nominal endings) and kṛt-affixes) — roRI

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.78"
SUTRA_TEXT = "रोणी"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — roRI"


class Sutra4278:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.78: अग्निः'),
		('रामः', '', 'प.4.2.78: रामः'),
		('सीता', '', 'प.4.2.78: सीता'),
	]

