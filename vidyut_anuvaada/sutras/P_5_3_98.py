# Sutra प.5.3.98: लुम्मनुष्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — lummanuzye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.98"
SUTRA_TEXT = "लुम्मनुष्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — lummanuzye"


class Sutra5398:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.98: अग्निः'),
		('रामः', '', 'प.5.3.98: रामः'),
		('सीता', '', 'प.5.3.98: सीता'),
	]

