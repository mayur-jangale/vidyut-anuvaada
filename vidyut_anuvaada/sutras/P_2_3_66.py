# Sutra प.2.3.66: उभयप्राप्तौ कर्मणि
# (Samasa (compound formation)) — uBayaprAptO karmaRi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.66"
SUTRA_TEXT = "उभयप्राप्तौ कर्मणि"
SUTRA_DESC = "(Samasa (compound formation)) — uBayaprAptO karmaRi"


class Sutra2366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

