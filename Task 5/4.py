
import re
vowels = "aeiou"
random_Str = "qwrtypsdfghjklzxcvbnm"
res = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (random_Str, vowels, random_Str), input(), flags = re.IGNORECASE)
print('\n'.join(res or ['-1']))