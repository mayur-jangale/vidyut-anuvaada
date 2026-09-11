# Sutra प.5.3.31: उपर्युपरिष्टात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uparyuparizwAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.31"
SUTRA_TEXT = "उपर्युपरिष्टात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uparyuparizwAt"


class Sutra5331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.31: अग्निः'),
		('रामः', '', 'प.5.3.31: रामः'),
		('सीता', '', 'प.5.3.31: सीता'),
	]

