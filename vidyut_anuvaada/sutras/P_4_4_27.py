# Sutra प.4.4.27: ओजस्सहोऽम्भसा वर्तते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ojassaho'mBasA vartate

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.27"
SUTRA_TEXT = "ओजस्सहोऽम्भसा वर्तते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ojassaho'mBasA vartate"


class Sutra4427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.27: अग्निः'),
		('रामः', '', 'प.4.4.27: रामः'),
		('सीता', '', 'प.4.4.27: सीता'),
	]

