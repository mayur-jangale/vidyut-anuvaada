# Sutra प.4.2.15: स्थण्डिलाच्छयितरि व्रते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sTaRqilAcCayitari vrate

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.15"
SUTRA_TEXT = "स्थण्डिलाच्छयितरि व्रते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sTaRqilAcCayitari vrate"


class Sutra4215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.15: अग्निः'),
		('रामः', '', 'प.4.2.15: रामः'),
		('सीता', '', 'प.4.2.15: सीता'),
	]

