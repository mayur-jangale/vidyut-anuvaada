# Sutra प.5.3.7: पञ्चम्यास्तसिल्
# ka — diminutive

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.7"
SUTRA_TEXT = "पञ्चम्यास्तसिल्"
SUTRA_DESC = "ka — diminutive"


class Sutra537:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.7: अग्निः'),
		('रामः', '', 'प.5.3.7: रामः'),
		('सीता', '', 'प.5.3.7: सीता'),
	]

