# Sutra प.4.3.67: बह्वचोऽन्तोदात्ताट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — bahvaco'ntodAttAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.67"
SUTRA_TEXT = "बह्वचोऽन्तोदात्ताट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — bahvaco'ntodAttAwWaY"


class Sutra4367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.67: अग्निः'),
		('रामः', '', 'प.4.3.67: रामः'),
		('सीता', '', 'प.4.3.67: सीता'),
	]

