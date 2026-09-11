# Sutra प.4.4.143: शिवशमरिष्टस्य करे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SivaSamarizwasya kare

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.143"
SUTRA_TEXT = "शिवशमरिष्टस्य करे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SivaSamarizwasya kare"


class Sutra44143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.143: अग्निः'),
		('रामः', '', 'प.4.4.143: रामः'),
		('सीता', '', 'प.4.4.143: सीता'),
	]

