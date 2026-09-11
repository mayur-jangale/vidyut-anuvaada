# Sutra प.4.3.58: गम्भीराञ्ञ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gamBIrAYYyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.58"
SUTRA_TEXT = "गम्भीराञ्ञ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gamBIrAYYyaH"


class Sutra4358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.58: अग्निः'),
		('रामः', '', 'प.4.3.58: रामः'),
		('सीता', '', 'प.4.3.58: सीता'),
	]

