# Sutra प.4.3.47: देयमृणे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — deyamfRe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.47"
SUTRA_TEXT = "देयमृणे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — deyamfRe"


class Sutra4347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.47: अग्निः'),
		('रामः', '', 'प.4.3.47: रामः'),
		('सीता', '', 'प.4.3.47: सीता'),
	]

