# Sutra प.8.2.88: ये यज्ञकर्मणि
# (Final transformations (tripāḍī)) — ye yajYakarmaRi

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.88"
SUTRA_TEXT = "ये यज्ञकर्मणि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — ye yajYakarmaRi"


class Sutra8288:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.88: अग्निः'),
		('रामः', '', 'प.8.2.88: रामः'),
		('सीता', '', 'प.8.2.88: सीता'),
	]

