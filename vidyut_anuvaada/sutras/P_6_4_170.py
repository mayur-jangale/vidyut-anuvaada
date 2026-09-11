# Sutra प.6.4.170: न मपूर्वोऽपत्येऽवर्मणः
# (Sandhi (euphonic combination)) — na mapUrvo'patye'varmaRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.170"
SUTRA_TEXT = "न मपूर्वोऽपत्येऽवर्मणः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — na mapUrvo'patye'varmaRaH"


class Sutra64170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.170: अग्निः'),
		('रामः', '', 'प.6.4.170: रामः'),
		('सीता', '', 'प.6.4.170: सीता'),
	]

