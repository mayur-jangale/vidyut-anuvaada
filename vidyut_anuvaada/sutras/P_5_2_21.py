# Sutra प.5.2.21: व्रातेन जीवति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrAtena jIvati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.21"
SUTRA_TEXT = "व्रातेन जीवति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrAtena jIvati"


class Sutra5221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.21: अग्निः'),
		('रामः', '', 'प.5.2.21: रामः'),
		('सीता', '', 'प.5.2.21: सीता'),
	]

