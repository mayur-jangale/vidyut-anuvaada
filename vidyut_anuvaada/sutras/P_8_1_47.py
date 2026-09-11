# Sutra प.8.1.47: जात्वपूर्वम्
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.47"
SUTRA_TEXT = "जात्वपूर्वम्"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.47: अग्निः'),
		('रामः', '', 'प.8.1.47: रामः'),
		('सीता', '', 'प.8.1.47: सीता'),
	]

