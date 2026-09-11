# Sutra प.4.4.48: अण् महिष्यादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aR mahizyAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.48"
SUTRA_TEXT = "अण् महिष्यादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aR mahizyAdiByaH"


class Sutra4448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.48: अग्निः'),
		('रामः', '', 'प.4.4.48: रामः'),
		('सीता', '', 'प.4.4.48: सीता'),
	]

