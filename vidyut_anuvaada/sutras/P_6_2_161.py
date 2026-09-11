# Sutra प.6.2.161: विभाषा तृन्नन्नतीक्ष्णशुचिषु
# (Sandhi (euphonic combination)) — viBAzA tfnnannatIkzRaSucizu

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.161"
SUTRA_TEXT = "विभाषा तृन्नन्नतीक्ष्णशुचिषु"
SUTRA_DESC = "(Sandhi (euphonic combination)) — viBAzA tfnnannatIkzRaSucizu"


class Sutra62161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.161: अग्निः'),
		('रामः', '', 'प.6.2.161: रामः'),
		('सीता', '', 'प.6.2.161: सीता'),
	]

