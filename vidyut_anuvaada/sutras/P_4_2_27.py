# Sutra प.4.2.27: अपोनप्त्रपान्नप्तृभ्यां घः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aponaptrapAnnaptfByAM GaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.27"
SUTRA_TEXT = "अपोनप्त्रपान्नप्तृभ्यां घः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aponaptrapAnnaptfByAM GaH"


class Sutra4227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.27: अग्निः'),
		('रामः', '', 'प.4.2.27: रामः'),
		('सीता', '', 'प.4.2.27: सीता'),
	]

