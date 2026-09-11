# Sutra प.7.2.28: रुष्यमत्वरसंघुषास्वनाम्
# (Taddhita (secondary derivations)) — ruzyamatvarasaMGuzAsvanAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.28"
SUTRA_TEXT = "रुष्यमत्वरसंघुषास्वनाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ruzyamatvarasaMGuzAsvanAm"


class Sutra7228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.28: अग्निः'),
		('रामः', '', 'प.7.2.28: रामः'),
		('सीता', '', 'प.7.2.28: सीता'),
	]

