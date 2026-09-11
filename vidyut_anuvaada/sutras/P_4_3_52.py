# Sutra प.4.3.52: तदस्य सोढम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadasya soQam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.52"
SUTRA_TEXT = "तदस्य सोढम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadasya soQam"


class Sutra4352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.52: अग्निः'),
		('रामः', '', 'प.4.3.52: रामः'),
		('सीता', '', 'प.4.3.52: सीता'),
	]

