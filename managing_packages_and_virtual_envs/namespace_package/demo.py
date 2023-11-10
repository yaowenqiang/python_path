import sys
sys.path.extend(['./path1', './path2'])
import demo_reader
print(demo_reader.__path__)
import demo_reader.util
import demo_reader.compressed

print(demo_reader.util.__path__)
print(demo_reader.compressed.__path__)
