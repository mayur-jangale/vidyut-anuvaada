# Sutra प.5.3.88: कुटीशमीशुण्डाभ्यो रः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kuwISamISuRqAByo raH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.88"
SUTRA_TEXT = "कुटीशमीशुण्डाभ्यो रः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kuwISamISuRqAByo raH"


class Sutra5388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.88: अग्निः'),
		('रामः', '', 'प.5.3.88: रामः'),
		('सीता', '', 'प.5.3.88: सीता'),
	]

