# Sutra प.5.4.18: द्वित्रिचतुर्भ्यः सुच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitricaturByaH suc

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.18"
SUTRA_TEXT = "द्वित्रिचतुर्भ्यः सुच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitricaturByaH suc"


class Sutra5418:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.18: अग्निः'),
		('रामः', '', 'प.5.4.18: रामः'),
		('सीता', '', 'प.5.4.18: सीता'),
	]

