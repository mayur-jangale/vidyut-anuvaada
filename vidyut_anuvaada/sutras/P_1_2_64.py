# Sutra प.1.2.64: सरूपाणामेकशेष एकविभक्तौ
# (Samjna (technical definitions)) — sarUpARAmekaSeza ekaviBaktO

from P_1_2 import apply_1_2_64

SUTRA_CODE = "प.1.2.64"
SUTRA_TEXT = "सरूपाणामेकशेष एकविभक्तौ"
SUTRA_DESC = "(Samjna (technical definitions)) — sarUpARAmekaSeza ekaviBaktO"


class Sutra1264:
	def apply(self, word, pos):
		return apply_1_2_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-ekaśeṣa:अग्निः'),
		('रामः', '', 'non-ekaśeṣa:रामः'),
		('सीता', '', 'non-ekaśeṣa:सीता'),
	]

