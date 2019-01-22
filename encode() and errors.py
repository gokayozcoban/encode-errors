
# encode() METOD and errors

##print("Bu Türkçe bir cümledir.".encode("ascii",errors="strict"))

##Traceback (most recent call last):
##  File "D:/PYTHON/Çalışmalar code000/CODE73 4 character encoding UTF-8 kod
##çözücü 2.py", line 15, in <module>
##    print("Bu Türkçe bir cümledir.".encode("ascii",errors="strict"))
##UnicodeEncodeError: 'ascii' codec can't encode character '\xfc' in position
##4: ordinal not in range(128)



print("Bu Türkçe bir cümledir.".encode("ascii",errors="ignore"))

#b'Bu Trke bir cmledir.



print("Bu Türkçe bir cümledir.".encode("ascii",errors="replace"))

#b'Bu T?rk?e bi c?mledir.'



print("Bu Türkçe bir cümledir.".encode("ascii",errors="xmlcharrefreplace"))

#b'Bu T&#252;rk&#231;e bir c&#252;mledir.'
