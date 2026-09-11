# Sutra प.8.1.45: लोपे विभाषा
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.45"
SUTRA_TEXT = "लोपे विभाषा"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.45: अग्निः'),
		('रामः', '', 'प.8.1.45: रामः'),
		('सीता', '', 'प.8.1.45: सीता'),
	]

