# Sutra प.5.4.126: दक्षिणेर्मा लुब्धयोगे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dakziRermA lubDayoge

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.126"
SUTRA_TEXT = "दक्षिणेर्मा लुब्धयोगे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dakziRermA lubDayoge"


class Sutra54126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.126: अग्निः'),
		('रामः', '', 'प.5.4.126: रामः'),
		('सीता', '', 'प.5.4.126: सीता'),
	]

