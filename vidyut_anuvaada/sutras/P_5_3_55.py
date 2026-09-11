# Sutra प.5.3.55: अतिशायने तमबिष्ठनौ
# tar, tama — comparative/superlative

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.55"
SUTRA_TEXT = "अतिशायने तमबिष्ठनौ"
SUTRA_DESC = "tar, tama — comparative/superlative"


class Sutra5355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.55: अग्निः'),
		('रामः', '', 'प.5.3.55: रामः'),
		('सीता', '', 'प.5.3.55: सीता'),
	]

