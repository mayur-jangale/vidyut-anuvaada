# Sutra प.8.1.35: छन्दस्यनेकमपि साकाङ्क्षम्
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.35"
SUTRA_TEXT = "छन्दस्यनेकमपि साकाङ्क्षम्"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.35: अग्निः'),
		('रामः', '', 'प.8.1.35: रामः'),
		('सीता', '', 'प.8.1.35: सीता'),
	]

