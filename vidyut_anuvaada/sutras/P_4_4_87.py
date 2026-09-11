# Sutra प.4.4.87: पदमस्मिन् दृश्यम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — padamasmin dfSyam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.87"
SUTRA_TEXT = "पदमस्मिन् दृश्यम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — padamasmin dfSyam"


class Sutra4487:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.87: अग्निः'),
		('रामः', '', 'प.4.4.87: रामः'),
		('सीता', '', 'प.4.4.87: सीता'),
	]

