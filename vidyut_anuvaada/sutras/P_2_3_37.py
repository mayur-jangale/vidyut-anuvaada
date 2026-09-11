# Sutra प.2.3.37: यस्य च भावेन भावलक्षणम्
# (Samasa (compound formation)) — yasya ca BAvena BAvalakzaRam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.37"
SUTRA_TEXT = "यस्य च भावेन भावलक्षणम्"
SUTRA_DESC = "(Samasa (compound formation)) — yasya ca BAvena BAvalakzaRam"


class Sutra2337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

