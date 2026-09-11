# Sutra प.4.4.36: परिपन्थं च तिष्ठति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — paripanTaM ca tizWati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.36"
SUTRA_TEXT = "परिपन्थं च तिष्ठति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — paripanTaM ca tizWati"


class Sutra4436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.36: अग्निः'),
		('रामः', '', 'प.4.4.36: रामः'),
		('सीता', '', 'प.4.4.36: सीता'),
	]

