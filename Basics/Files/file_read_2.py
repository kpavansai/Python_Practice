from os.path import dirname

SAMPLE_FILE = open(dirname(__file__) + "/sample.txt", "r")
print(SAMPLE_FILE.read(10))
print(SAMPLE_FILE.tell())
print(SAMPLE_FILE.read(10))
print(SAMPLE_FILE.tell())
SAMPLE_FILE.seek(0, 0)
print(SAMPLE_FILE.tell())
print(SAMPLE_FILE.read(10))
print(SAMPLE_FILE.tell())
print(SAMPLE_FILE.read(10))
print(SAMPLE_FILE.tell())
