# Sutra प.6.4.37: अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक लोपो झलि क्ङिति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.37"
SUTRA_TEXT = "अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक लोपो झलि क्ङिति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.37: अग्निः'),
		('रामः', '', 'प.6.4.37: रामः'),
		('सीता', '', 'प.6.4.37: सीता'),
	]

