# Sutra प.4.4.51: तदस्य पण्यम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadasya paRyam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.51"
SUTRA_TEXT = "तदस्य पण्यम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadasya paRyam"


class Sutra4451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.51: अग्निः'),
		('रामः', '', 'प.4.4.51: रामः'),
		('सीता', '', 'प.4.4.51: सीता'),
	]

