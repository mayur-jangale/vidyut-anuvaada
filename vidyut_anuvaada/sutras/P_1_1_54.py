# Sutra प.1.1.54: आदेः परस्य
# (Samjna (technical definitions)) — AdeH parasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.54"
SUTRA_TEXT = "आदेः परस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — AdeH parasya"


class Sutra1154:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_54
		return apply_1_1_54(word, pos)

	EXAMPLES = [
		('आदेः', '', 'प.1.1.54:ādeḥ-parasya;input=आदेः'),
		('अग्नि', '', 'प.1.1.54:ādeḥ-parasya;input=अग्नि'),
	]

