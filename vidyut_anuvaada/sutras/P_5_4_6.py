# Sutra प.5.4.6: बृहत्या आच्छादने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bfhatyA AcCAdane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.6"
SUTRA_TEXT = "बृहत्या आच्छादने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bfhatyA AcCAdane"


class Sutra546:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.6: अग्निः'),
		('रामः', '', 'प.5.4.6: रामः'),
		('सीता', '', 'प.5.4.6: सीता'),
	]

