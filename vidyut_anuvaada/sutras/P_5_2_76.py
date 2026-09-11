# Sutra प.5.2.76: अयःशूलदण्डाजिनाभ्यां ठक्ठञौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ayaHSUladaRqAjinAByAM WakWaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.76"
SUTRA_TEXT = "अयःशूलदण्डाजिनाभ्यां ठक्ठञौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ayaHSUladaRqAjinAByAM WakWaYO"


class Sutra5276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.76: अग्निः'),
		('रामः', '', 'प.5.2.76: रामः'),
		('सीता', '', 'प.5.2.76: सीता'),
	]

