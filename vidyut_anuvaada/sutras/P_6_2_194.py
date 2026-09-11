# Sutra प.6.2.194: उपाद् द्व्यजजिनमगौरादयः
# (Sandhi (euphonic combination)) — upAd dvyajajinamagOrAdayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.194"
SUTRA_TEXT = "उपाद् द्व्यजजिनमगौरादयः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — upAd dvyajajinamagOrAdayaH"


class Sutra62194:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.194: अग्निः'),
		('रामः', '', 'प.6.2.194: रामः'),
		('सीता', '', 'प.6.2.194: सीता'),
	]

