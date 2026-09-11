# Sutra प.7.1.39: सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः
# (Taddhita (secondary derivations)) — supAM sulukpUrvasavarRA''cCeyAqAqyAyAjAlaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.39"
SUTRA_TEXT = "सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — supAM sulukpUrvasavarRA''cCeyAqAqyAyAjAlaH"


class Sutra7139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.39: अग्निः'),
		('रामः', '', 'प.7.1.39: रामः'),
		('सीता', '', 'प.7.1.39: सीता'),
	]

