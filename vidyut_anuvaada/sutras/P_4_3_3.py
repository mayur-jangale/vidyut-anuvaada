# Sutra प.4.3.3: तवकममकावेकवचने
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tavakamamakAvekavacane

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.3"
SUTRA_TEXT = "तवकममकावेकवचने"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tavakamamakAvekavacane"


class Sutra433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.3: अग्निः'),
		('रामः', '', 'प.4.3.3: रामः'),
		('सीता', '', 'प.4.3.3: सीता'),
	]

