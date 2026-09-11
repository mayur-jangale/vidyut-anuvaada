# Sutra प.5.4.40: सस्नौ प्रशंसायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sasnO praSaMsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.40"
SUTRA_TEXT = "सस्नौ प्रशंसायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sasnO praSaMsAyAm"


class Sutra5440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.40: अग्निः'),
		('रामः', '', 'प.5.4.40: रामः'),
		('सीता', '', 'प.5.4.40: सीता'),
	]

