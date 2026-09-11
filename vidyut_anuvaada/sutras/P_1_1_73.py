# Sutra प.1.1.73: वृद्धिर्यस्याचामादिस्तद् वृद्धम्
# (Samjna (technical definitions)) — vfdDiryasyAcAmAdistad vfdDam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.73"
SUTRA_TEXT = "वृद्धिर्यस्याचामादिस्तद् वृद्धम्"
SUTRA_DESC = "(Samjna (technical definitions)) — vfdDiryasyAcAmAdistad vfdDam"


class Sutra1173:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_73
		return apply_1_1_73(word, pos)

	EXAMPLES = [
		('आगच्छ', '', 'वृद्धम्-prefix:आगच्छ'),
		('इदम्', '', 'non-vṛddha:इदम्'),
		('पश्य', '', 'non-vṛddha:पश्य'),
	]

