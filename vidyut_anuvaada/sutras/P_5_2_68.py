# Sutra प.5.2.68: सस्येन परिजातः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sasyena parijAtaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.68"
SUTRA_TEXT = "सस्येन परिजातः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sasyena parijAtaH"


class Sutra5268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.68: अग्निः'),
		('रामः', '', 'प.5.2.68: रामः'),
		('सीता', '', 'प.5.2.68: सीता'),
	]

