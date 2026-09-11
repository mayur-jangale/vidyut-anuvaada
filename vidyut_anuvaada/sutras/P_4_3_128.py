# Sutra प.4.3.128: शाकलाद्वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SAkalAdvA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.128"
SUTRA_TEXT = "शाकलाद्वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SAkalAdvA"


class Sutra43128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.128: अग्निः'),
		('रामः', '', 'प.4.3.128: रामः'),
		('सीता', '', 'प.4.3.128: सीता'),
	]

