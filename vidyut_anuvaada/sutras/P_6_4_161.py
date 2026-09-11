# Sutra प.6.4.161: र ऋतो हलादेर्लघोः
# (Sandhi (euphonic combination)) — ra fto halAderlaGoH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.161"
SUTRA_TEXT = "र ऋतो हलादेर्लघोः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — ra fto halAderlaGoH"


class Sutra64161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.161: अग्निः'),
		('रामः', '', 'प.6.4.161: रामः'),
		('सीता', '', 'प.6.4.161: सीता'),
	]

