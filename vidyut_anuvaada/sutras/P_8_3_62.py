# Sutra प.8.3.62: सः स्विदिस्वदिसहीनां च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.62"
SUTRA_TEXT = "सः स्विदिस्वदिसहीनां च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.62: अग्निः'),
		('रामः', '', 'प.8.3.62: रामः'),
		('सीता', '', 'प.8.3.62: सीता'),
	]

