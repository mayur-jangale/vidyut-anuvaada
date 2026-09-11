# Sutra प.6.2.24: विस्पष्टादीनि गुणवचनेषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.24"
SUTRA_TEXT = "विस्पष्टादीनि गुणवचनेषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.24: अग्निः'),
		('रामः', '', 'प.6.2.24: रामः'),
		('सीता', '', 'प.6.2.24: सीता'),
	]

