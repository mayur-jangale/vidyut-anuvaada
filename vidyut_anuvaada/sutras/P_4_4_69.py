# Sutra प.4.4.69: तत्र नियुक्तः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tatra niyuktaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.69"
SUTRA_TEXT = "तत्र नियुक्तः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tatra niyuktaH"


class Sutra4469:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.69: अग्निः'),
		('रामः', '', 'प.4.4.69: रामः'),
		('सीता', '', 'प.4.4.69: सीता'),
	]

