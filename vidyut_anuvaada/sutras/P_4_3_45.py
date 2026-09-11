# Sutra प.4.3.45: आश्वयुज्या वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ASvayujyA vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.45"
SUTRA_TEXT = "आश्वयुज्या वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ASvayujyA vuY"


class Sutra4345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.45: अग्निः'),
		('रामः', '', 'प.4.3.45: रामः'),
		('सीता', '', 'प.4.3.45: सीता'),
	]

