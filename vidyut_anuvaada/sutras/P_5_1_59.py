# Sutra प.5.1.59: पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paNktiviMSatitriMSatcatvAriMSatpaYcASatzazwisaptatyaSItinavatiSatam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.59"
SUTRA_TEXT = "पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paNktiviMSatitriMSatcatvAriMSatpaYcASatzazwisaptatyaSItinavatiSatam"


class Sutra5159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.59: अग्निः'),
		('रामः', '', 'प.5.1.59: रामः'),
		('सीता', '', 'प.5.1.59: सीता'),
	]

