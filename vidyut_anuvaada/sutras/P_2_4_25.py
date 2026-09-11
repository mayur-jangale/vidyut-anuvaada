# Sutra प.2.4.25: विभाषा सेनासुराच्छायाशालानिशानाम्
# (Samasa (compound formation)) — viBAzA senAsurAcCAyASAlAniSAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.25"
SUTRA_TEXT = "विभाषा सेनासुराच्छायाशालानिशानाम्"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA senAsurAcCAyASAlAniSAnAm"


class Sutra2425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

