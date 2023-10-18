import os
import stat

f = open('foo.txt', 'w')
s = os.stat('foo.txt')
print(bin(s.st_mode))
print(s.st_mode & stat.S_IWUSR) # non-zero menas the file is writable for the user
print(s.st_mode & stat.S_IXUSR) # non-zero menas the file is writable for the user

is_writable_by_other_users = bool(s.st_mode & stat.S_IWOTH)
print(is_writable_by_other_users)
