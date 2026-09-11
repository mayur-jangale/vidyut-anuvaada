# Sutra प.4.4.140: वसोः समूहे च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vasoH samUhe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.140"
SUTRA_TEXT = "वसोः समूहे च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vasoH samUhe ca"


class Sutra44140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.140: अग्निः'),
		('रामः', '', 'प.4.4.140: रामः'),
		('सीता', '', 'प.4.4.140: सीता'),
	]

