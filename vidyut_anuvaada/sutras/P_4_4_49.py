# Sutra प.4.4.49: ऋतोऽञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — fto'Y

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.49"
SUTRA_TEXT = "ऋतोऽञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — fto'Y"


class Sutra4449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.49: अग्निः'),
		('रामः', '', 'प.4.4.49: रामः'),
		('सीता', '', 'प.4.4.49: सीता'),
	]

