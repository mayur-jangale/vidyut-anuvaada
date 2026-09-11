# Sutra प.4.3.12: श्राद्धे शरदः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SrAdDe SaradaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.12"
SUTRA_TEXT = "श्राद्धे शरदः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SrAdDe SaradaH"


class Sutra4312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.12: अग्निः'),
		('रामः', '', 'प.4.3.12: रामः'),
		('सीता', '', 'प.4.3.12: सीता'),
	]

