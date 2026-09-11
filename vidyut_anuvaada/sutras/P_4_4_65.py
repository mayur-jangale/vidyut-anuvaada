# Sutra प.4.4.65: हितं भक्षाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — hitaM BakzAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.65"
SUTRA_TEXT = "हितं भक्षाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — hitaM BakzAH"


class Sutra4465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.65: अग्निः'),
		('रामः', '', 'प.4.4.65: रामः'),
		('सीता', '', 'प.4.4.65: सीता'),
	]

