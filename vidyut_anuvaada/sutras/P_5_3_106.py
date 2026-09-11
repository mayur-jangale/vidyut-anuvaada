# Sutra प.5.3.106: समासाच्च तद्विषयात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAsAcca tadvizayAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.106"
SUTRA_TEXT = "समासाच्च तद्विषयात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAsAcca tadvizayAt"


class Sutra53106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.106: अग्निः'),
		('रामः', '', 'प.5.3.106: रामः'),
		('सीता', '', 'प.5.3.106: सीता'),
	]

