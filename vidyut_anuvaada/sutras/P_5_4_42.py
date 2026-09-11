# Sutra प.5.4.42: बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahvalpArTAcCas kArakAdanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.42"
SUTRA_TEXT = "बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahvalpArTAcCas kArakAdanyatarasyAm"


class Sutra5442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.42: अग्निः'),
		('रामः', '', 'प.5.4.42: रामः'),
		('सीता', '', 'प.5.4.42: सीता'),
	]

