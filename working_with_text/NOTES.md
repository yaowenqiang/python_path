mode | buffering | Result
-    | -------- | ----- |
any binary |  0 |  FileIo
'rb' |  !=0 |  BufferedReader
'wb', 'ab' |  != 0 |  BufferedWritter
'rb+', 'wb+', 'ab+' |  != 0 |  BufferedRandom
any text |  != 0 |  TextIoWrapper
