# Sutra प.2.3.56: जासिनिप्रहणनाटक्राथपिषां हिंसायाम्
# (Samasa (compound formation)) — jAsiniprahaRanAwakrATapizAM hiMsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.56"
SUTRA_TEXT = "जासिनिप्रहणनाटक्राथपिषां हिंसायाम्"
SUTRA_DESC = "(Samasa (compound formation)) — jAsiniprahaRanAwakrATapizAM hiMsAyAm"


class Sutra2356:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

