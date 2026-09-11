# Sutra प.4.3.89: सोऽस्य निवासः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — so'sya nivAsaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.89"
SUTRA_TEXT = "सोऽस्य निवासः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — so'sya nivAsaH"


class Sutra4389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.89: अग्निः'),
		('रामः', '', 'प.4.3.89: रामः'),
		('सीता', '', 'प.4.3.89: सीता'),
	]

