# Sutra प.4.2.103: वर्णौ वुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — varRO vuk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.103"
SUTRA_TEXT = "वर्णौ वुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — varRO vuk"


class Sutra42103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.103: अग्निः'),
		('रामः', '', 'प.4.2.103: रामः'),
		('सीता', '', 'प.4.2.103: सीता'),
	]

