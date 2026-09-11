# Sutra प.4.3.157: उष्ट्राद्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — uzwrAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.157"
SUTRA_TEXT = "उष्ट्राद्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — uzwrAdvuY"


class Sutra43157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.157: अग्निः'),
		('रामः', '', 'प.4.3.157: रामः'),
		('सीता', '', 'प.4.3.157: सीता'),
	]

