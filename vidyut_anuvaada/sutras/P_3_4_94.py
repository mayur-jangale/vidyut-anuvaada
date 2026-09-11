# Sutra प.3.4.94: लेटोऽडाटौ
# liṅāśiṣi — liṅ in āśīr sense is ardhādhātuka

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.94"
SUTRA_TEXT = "लेटोऽडाटौ"
SUTRA_DESC = "liṅāśiṣi — liṅ in āśīr sense is ardhādhātuka"


class Sutra3494:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

