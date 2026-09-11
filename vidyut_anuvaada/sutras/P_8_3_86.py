# Sutra प.8.3.86: अभिनिसः स्तनः शब्दसंज्ञायाम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.86"
SUTRA_TEXT = "अभिनिसः स्तनः शब्दसंज्ञायाम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8386:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.86: अग्निः'),
		('रामः', '', 'प.8.3.86: रामः'),
		('सीता', '', 'प.8.3.86: सीता'),
	]

