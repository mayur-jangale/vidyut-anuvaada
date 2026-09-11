# Sutra प.8.2.19: उपसर्गस्यायतौ
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.19"
SUTRA_TEXT = "उपसर्गस्यायतौ"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8219:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.19: अग्निः'),
		('रामः', '', 'प.8.2.19: रामः'),
		('सीता', '', 'प.8.2.19: सीता'),
	]

