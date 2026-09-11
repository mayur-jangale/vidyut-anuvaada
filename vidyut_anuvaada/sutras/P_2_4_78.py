# Sutra प.2.4.78: विभाषा घ्राधेट्शाच्छासः
# (Samasa (compound formation)) — viBAzA GrADewSAcCAsaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.78"
SUTRA_TEXT = "विभाषा घ्राधेट्शाच्छासः"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA GrADewSAcCAsaH"


class Sutra2478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

