from pydub import AudioSegment
from gtts import gTTS

# Create a gTTS object
tts = gTTS("""
Dzień dobry!
Witaj w Małopolskim Centrum Nauki Cogiteon. Informujemy, że rozmowy mogą być nagrywane. Administratorem danych osobowych jest Małopolskie Centrum Nauki Cogiteon z siedzibą w Krakowie. Szczegółowe informacje o przetwarzaniu danych osobowych znajdziesz na naszej stronie internetowej.
Jeśli chcesz dowiedzieć się więcej o naszych aktualnych wystawach, warsztatach lub wydarzeniach, zapraszamy na naszą stronę internetową www.cogiteon.pl.

Cogiteon to miejsce pełne interaktywnych atrakcji, które pozwalają odkrywać, eksperymentować i doświadczyć nauki w nowatorski sposób. Nasza stała wystawa „Człowiek i jego marzenia” oferuje ponad sto interaktywnych stanowisk rozlokowanych na przestrzeni ponad 2,2 tys. m2, a nasze laboratoria zapraszają do udziału w fascynujących warsztatach, takich jak „Laboratorium Smaków” czy „Laboratorium Przyrody”.
Dla dodatkowych informacji, prosimy odwiedzić naszą stronę www.cogiteon.pl lub skontaktować się z nami poprzez e-mail: oferta@cogiteon.pl.
Jeśli potrzebujesz informacji na temat oferty indywidualnej wciśnij 1
Jeśli potrzebujesz informacji na temat oferty dla firm wciśnij 2
Jeśli potrzebujesz innych informacji wciśnij 3

Dziękujemy za telefon i zapraszamy do odkrywania tajemnic nauki z Cogiteon!
""", lang='pl', tld='com.pl', slow=False)

# Save the spoken text to an mp3 file
tts.save('hello.mp3')

audio = AudioSegment.from_mp3('hello.mp3')

audio.speedup(playback_speed=3.0)

audio.export("asd.mp3", format='mp3')