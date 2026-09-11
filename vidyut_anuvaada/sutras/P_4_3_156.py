# Sutra प.4.3.156: क्रीतवत् परिमाणात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — krItavat parimARAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.156"
SUTRA_TEXT = "क्रीतवत् परिमाणात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — krItavat parimARAt"


class Sutra43156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.156: अग्निः'),
		('रामः', '', 'प.4.3.156: रामः'),
		('सीता', '', 'प.4.3.156: सीता'),
	]

