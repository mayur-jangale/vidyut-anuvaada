# Sutra प.5.4.30: लोहितान्मणौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — lohitAnmaRO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.30"
SUTRA_TEXT = "लोहितान्मणौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — lohitAnmaRO"


class Sutra5430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.30: अग्निः'),
		('रामः', '', 'प.5.4.30: रामः'),
		('सीता', '', 'प.5.4.30: सीता'),
	]

