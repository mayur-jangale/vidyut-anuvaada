# Sutra प.5.2.29: सम्प्रोदश्च कटच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samprodaSca kawac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.29"
SUTRA_TEXT = "सम्प्रोदश्च कटच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samprodaSca kawac"


class Sutra5229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.29: अग्निः'),
		('रामः', '', 'प.5.2.29: रामः'),
		('सीता', '', 'प.5.2.29: सीता'),
	]

