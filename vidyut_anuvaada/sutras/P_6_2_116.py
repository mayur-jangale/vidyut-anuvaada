# Sutra प.6.2.116: नञो जरमरमित्रमृताः
# (Sandhi (euphonic combination)) — naYo jaramaramitramftAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.116"
SUTRA_TEXT = "नञो जरमरमित्रमृताः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — naYo jaramaramitramftAH"


class Sutra62116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.116: अग्निः'),
		('रामः', '', 'प.6.2.116: रामः'),
		('सीता', '', 'प.6.2.116: सीता'),
	]

