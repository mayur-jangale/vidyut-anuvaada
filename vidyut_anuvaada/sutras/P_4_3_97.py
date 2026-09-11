# Sutra प.4.3.97: महाराजाट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mahArAjAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.97"
SUTRA_TEXT = "महाराजाट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mahArAjAwWaY"


class Sutra4397:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.97: अग्निः'),
		('रामः', '', 'प.4.3.97: रामः'),
		('सीता', '', 'प.4.3.97: सीता'),
	]

