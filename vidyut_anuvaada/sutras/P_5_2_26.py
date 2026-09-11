# Sutra प.5.2.26: तेन वित्तश्चुञ्चुप्चणपौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena vittaScuYcupcaRapO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.26"
SUTRA_TEXT = "तेन वित्तश्चुञ्चुप्चणपौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena vittaScuYcupcaRapO"


class Sutra5226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.26: अग्निः'),
		('रामः', '', 'प.5.2.26: रामः'),
		('सीता', '', 'प.5.2.26: सीता'),
	]

