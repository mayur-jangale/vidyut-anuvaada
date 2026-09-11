# Sutra प.8.2.37: एकाचो बशो भष् झषन्तस्य स्ध्वोः
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.37"
SUTRA_TEXT = "एकाचो बशो भष् झषन्तस्य स्ध्वोः"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.37: अग्निः'),
		('रामः', '', 'प.8.2.37: रामः'),
		('सीता', '', 'प.8.2.37: सीता'),
	]

