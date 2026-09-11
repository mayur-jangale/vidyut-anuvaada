# Sutra प.8.2.11: संज्ञायाम्
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.11"
SUTRA_TEXT = "संज्ञायाम्"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.11: अग्निः'),
		('रामः', '', 'प.8.2.11: रामः'),
		('सीता', '', 'प.8.2.11: सीता'),
	]

