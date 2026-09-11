# Sutra प.6.4.165: गाथिविदथिकेशिगणिपणिनश्च
# (Sandhi (euphonic combination)) — gATividaTikeSigaRipaRinaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.165"
SUTRA_TEXT = "गाथिविदथिकेशिगणिपणिनश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — gATividaTikeSigaRipaRinaSca"


class Sutra64165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.165: अग्निः'),
		('रामः', '', 'प.6.4.165: रामः'),
		('सीता', '', 'प.6.4.165: सीता'),
	]

