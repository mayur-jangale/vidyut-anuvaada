# Sutra प.8.3.53: षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.53"
SUTRA_TEXT = "षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.53: अग्निः'),
		('रामः', '', 'प.8.3.53: रामः'),
		('सीता', '', 'प.8.3.53: सीता'),
	]

