# Sutra प.4.4.47: तस्य धर्म्यम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasya Darmyam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.47"
SUTRA_TEXT = "तस्य धर्म्यम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasya Darmyam"


class Sutra4447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.47: अग्निः'),
		('रामः', '', 'प.4.4.47: रामः'),
		('सीता', '', 'प.4.4.47: सीता'),
	]

