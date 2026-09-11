# Sutra प.5.3.78: बह्वचो मनुष्यनाम्नष्ठज्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahvaco manuzyanAmnazWajvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.78"
SUTRA_TEXT = "बह्वचो मनुष्यनाम्नष्ठज्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahvaco manuzyanAmnazWajvA"


class Sutra5378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.78: अग्निः'),
		('रामः', '', 'प.5.3.78: रामः'),
		('सीता', '', 'प.5.3.78: सीता'),
	]

