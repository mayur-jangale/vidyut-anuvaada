# Sutra प.8.1.57: चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.57"
SUTRA_TEXT = "चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.57: अग्निः'),
		('रामः', '', 'प.8.1.57: रामः'),
		('सीता', '', 'प.8.1.57: सीता'),
	]

