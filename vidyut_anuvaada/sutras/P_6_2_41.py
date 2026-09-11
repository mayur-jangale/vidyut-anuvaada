# Sutra प.6.2.41: गौः सादसादिसारथिषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.41"
SUTRA_TEXT = "गौः सादसादिसारथिषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.41: अग्निः'),
		('रामः', '', 'प.6.2.41: रामः'),
		('सीता', '', 'प.6.2.41: सीता'),
	]

