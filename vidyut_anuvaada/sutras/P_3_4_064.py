# Sutra प64: anvacyAnulomye
# anvacyAnulomye

from sutra_engines import apply_general
from P_3_4 import apply_3_4_64

SUTRA_CODE = "प64"
SUTRA_TEXT = "anvacyAnulomye"
SUTRA_DESC = "anvacyAnulomye"


class Sutra3464:
	def apply(self, word, pos):
		return apply_3_4_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-064:anvacyAnulomye;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-064:anvacyAnulomye;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-064:anvacyAnulomye;input=सीता;stem=सीता;ending=-;pos='),
	]

