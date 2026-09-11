# Sutra प.5.4.2: दण्डव्यवसर्गयोश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — daRqavyavasargayoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.2"
SUTRA_TEXT = "दण्डव्यवसर्गयोश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — daRqavyavasargayoSca"


class Sutra542:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.2: अग्निः'),
		('रामः', '', 'प.5.4.2: रामः'),
		('सीता', '', 'प.5.4.2: सीता'),
	]

