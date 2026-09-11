# Sutra प.8.3.78: इणः षीध्वंलुङ्लिटां धोऽङ्गात्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.78"
SUTRA_TEXT = "इणः षीध्वंलुङ्लिटां धोऽङ्गात्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.78: अग्निः'),
		('रामः', '', 'प.8.3.78: रामः'),
		('सीता', '', 'प.8.3.78: सीता'),
	]

