# Sutra प.2.3.54: रुजार्थानां भाववचनानामज्वरेः
# (Samasa (compound formation)) — rujArTAnAM BAvavacanAnAmajvareH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.54"
SUTRA_TEXT = "रुजार्थानां भाववचनानामज्वरेः"
SUTRA_DESC = "(Samasa (compound formation)) — rujArTAnAM BAvavacanAnAmajvareH"


class Sutra2354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

