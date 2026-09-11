# Sutra प.5.2.41: किमः संख्यापरिमाणे डति च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaH saMKyAparimARe qati ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.41"
SUTRA_TEXT = "किमः संख्यापरिमाणे डति च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaH saMKyAparimARe qati ca"


class Sutra5241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.41: अग्निः'),
		('रामः', '', 'प.5.2.41: रामः'),
		('सीता', '', 'प.5.2.41: सीता'),
	]

