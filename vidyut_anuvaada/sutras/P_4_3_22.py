# Sutra प.4.3.22: सर्वत्राण् च तलोपश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sarvatrAR ca talopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.22"
SUTRA_TEXT = "सर्वत्राण् च तलोपश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sarvatrAR ca talopaSca"


class Sutra4322:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.22: अग्निः'),
		('रामः', '', 'प.4.3.22: रामः'),
		('सीता', '', 'प.4.3.22: सीता'),
	]

