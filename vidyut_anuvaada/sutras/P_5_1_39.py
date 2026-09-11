# Sutra प.5.1.39: गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — godvyaco'saMKyAparimARASvAderyat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.39"
SUTRA_TEXT = "गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — godvyaco'saMKyAparimARASvAderyat"


class Sutra5139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.39: अग्निः'),
		('रामः', '', 'प.5.1.39: रामः'),
		('सीता', '', 'प.5.1.39: सीता'),
	]

