# Sutra प.1.1.36: अन्तरं बहिर्योगोपसंव्यानयोः
# (Samjna (technical definitions)) — antaraM bahiryogopasaMvyAnayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.36"
SUTRA_TEXT = "अन्तरं बहिर्योगोपसंव्यानयोः"
SUTRA_DESC = "(Samjna (technical definitions)) — antaraM bahiryogopasaMvyAnayoH"


class Sutra1136:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_36
		return apply_1_1_36(word, pos)

	EXAMPLES = [
		('अन्तरं', 'antar', 'antar=inside:अन्तरं'),
		('बहिः', 'bahir', 'bahir=outside:बहिः'),
		('देव', '', 'antar/bahir-context=no:देव'),
	]

