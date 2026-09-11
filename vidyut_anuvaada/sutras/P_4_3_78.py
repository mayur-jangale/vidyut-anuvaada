# Sutra प.4.3.78: ऋतष्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ftazWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.78"
SUTRA_TEXT = "ऋतष्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ftazWaY"


class Sutra4378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.78: अग्निः'),
		('रामः', '', 'प.4.3.78: रामः'),
		('सीता', '', 'प.4.3.78: सीता'),
	]

