str = "dGhpcyBpcyBObyBjaGVjayBmb3lgZW5jb2RllGFuZCBkZWNvZGU="
import base64
str_decoded = base64.b64decode(str)
print("The decoded string is:",str_decoded)
  