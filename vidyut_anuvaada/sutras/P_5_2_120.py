# Sutra प.5.2.120: रूपादाहतप्रशंसयोर्यप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rUpAdAhatapraSaMsayoryap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.120"
SUTRA_TEXT = "रूपादाहतप्रशंसयोर्यप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rUpAdAhatapraSaMsayoryap"


class Sutra52120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.120: अग्निः'),
		('रामः', '', 'प.5.2.120: रामः'),
		('सीता', '', 'प.5.2.120: सीता'),
	]

