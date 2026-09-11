# Sutra प.5.1.52: सम्भवत्यवहरति पचति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samBavatyavaharati pacati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.52"
SUTRA_TEXT = "सम्भवत्यवहरति पचति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samBavatyavaharati pacati"


class Sutra5152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.52: अग्निः'),
		('रामः', '', 'प.5.1.52: रामः'),
		('सीता', '', 'प.5.1.52: सीता'),
	]

