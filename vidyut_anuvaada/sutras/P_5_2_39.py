# Sutra प.5.2.39: यद्तदेतेभ्यः परिमाणे वतुप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yadtadeteByaH parimARe vatup

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.39"
SUTRA_TEXT = "यद्तदेतेभ्यः परिमाणे वतुप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yadtadeteByaH parimARe vatup"


class Sutra5239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.39: अग्निः'),
		('रामः', '', 'प.5.2.39: रामः'),
		('सीता', '', 'प.5.2.39: सीता'),
	]

