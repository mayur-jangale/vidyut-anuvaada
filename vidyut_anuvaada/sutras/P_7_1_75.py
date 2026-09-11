# Sutra प.7.1.75: अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः
# (Taddhita (secondary derivations)) — asTidaDisakTyakzRAmanaNudAttaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.75"
SUTRA_TEXT = "अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — asTidaDisakTyakzRAmanaNudAttaH"


class Sutra7175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.75: अग्निः'),
		('रामः', '', 'प.7.1.75: रामः'),
		('सीता', '', 'प.7.1.75: सीता'),
	]

