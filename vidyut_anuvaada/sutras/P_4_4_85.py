# Sutra प.4.4.85: अन्नाण्णः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — annARRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.85"
SUTRA_TEXT = "अन्नाण्णः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — annARRaH"


class Sutra4485:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.85: अग्निः'),
		('रामः', '', 'प.4.4.85: रामः'),
		('सीता', '', 'प.4.4.85: सीता'),
	]

