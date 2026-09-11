# Sutra प.1.1.41: अव्ययीभावश्च
# (Samjna (technical definitions)) — avyayIBAvaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.41"
SUTRA_TEXT = "अव्ययीभावश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — avyayIBAvaSca"


class Sutra1141:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_41
		return apply_1_1_41(word, pos)

	EXAMPLES = [
		('उप', '', 'avyayībhāva-head:उप'),
		('अनु', '', 'avyayībhāva-head:अनु'),
		('वि', '', 'avyayībhāva-head:वि'),
		('देव', '', 'not-head:देव'),
	]

