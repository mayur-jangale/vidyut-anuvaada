# Sutra प.5.4.86: तत्पुरुषस्याङ्गुलेः संख्याव्ययादेः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatpuruzasyANguleH saMKyAvyayAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.86"
SUTRA_TEXT = "तत्पुरुषस्याङ्गुलेः संख्याव्ययादेः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatpuruzasyANguleH saMKyAvyayAdeH"


class Sutra5486:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.86: अग्निः'),
		('रामः', '', 'प.5.4.86: रामः'),
		('सीता', '', 'प.5.4.86: सीता'),
	]

