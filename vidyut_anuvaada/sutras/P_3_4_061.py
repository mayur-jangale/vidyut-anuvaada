# Sutra प61: svANge taspratyaye kfBvoH
# svANge taspratyaye kfBvoH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_61

SUTRA_CODE = "प61"
SUTRA_TEXT = "svANge taspratyaye kfBvoH"
SUTRA_DESC = "svANge taspratyaye kfBvoH"


class Sutra3461:
	def apply(self, word, pos):
		return apply_3_4_61(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-061:svANge taspratyaye kfBvoH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-061:svANge taspratyaye kfBvoH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-061:svANge taspratyaye kfBvoH;input=सीता;stem=सीता;ending=-;pos='),
	]

