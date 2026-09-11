# Sutra प.4.2.33: अग्नेर्ढक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — agnerQak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.33"
SUTRA_TEXT = "अग्नेर्ढक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — agnerQak"


class Sutra4233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.33: अग्निः'),
		('रामः', '', 'प.4.2.33: रामः'),
		('सीता', '', 'प.4.2.33: सीता'),
	]

