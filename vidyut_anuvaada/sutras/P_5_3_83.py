# Sutra प.5.3.83: ठाजादावूर्ध्वं द्वितीयादचः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — WAjAdAvUrDvaM dvitIyAdacaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.83"
SUTRA_TEXT = "ठाजादावूर्ध्वं द्वितीयादचः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — WAjAdAvUrDvaM dvitIyAdacaH"


class Sutra5383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.83: अग्निः'),
		('रामः', '', 'प.5.3.83: रामः'),
		('सीता', '', 'प.5.3.83: सीता'),
	]

