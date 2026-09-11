# Sutra प.5.3.27: दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dikSabdeByaH saptamIpaYcamIpraTamAByo digdeSakAlezvastAtiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.27"
SUTRA_TEXT = "दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dikSabdeByaH saptamIpaYcamIpraTamAByo digdeSakAlezvastAtiH"


class Sutra5327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.27: अग्निः'),
		('रामः', '', 'प.5.3.27: रामः'),
		('सीता', '', 'प.5.3.27: सीता'),
	]

