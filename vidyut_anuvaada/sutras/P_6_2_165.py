# Sutra प.6.2.165: संज्ञायां मित्राजिनयोः
# (Sandhi (euphonic combination)) — saMjYAyAM mitrAjinayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.165"
SUTRA_TEXT = "संज्ञायां मित्राजिनयोः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMjYAyAM mitrAjinayoH"


class Sutra62165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.165: अग्निः'),
		('रामः', '', 'प.6.2.165: रामः'),
		('सीता', '', 'प.6.2.165: सीता'),
	]

