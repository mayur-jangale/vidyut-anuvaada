# Sutra प.6.3.135: द्व्यचोऽतस्तिङः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.135"
SUTRA_TEXT = "द्व्यचोऽतस्तिङः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.135: अग्निः'),
		('रामः', '', 'प.6.3.135: रामः'),
		('सीता', '', 'प.6.3.135: सीता'),
	]

