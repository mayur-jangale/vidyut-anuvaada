# Sutra प.5.3.85: अल्पे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — alpe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.85"
SUTRA_TEXT = "अल्पे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — alpe"


class Sutra5385:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.85: अग्निः'),
		('रामः', '', 'प.5.3.85: रामः'),
		('सीता', '', 'प.5.3.85: सीता'),
	]

