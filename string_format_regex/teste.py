n=int(input('digite o numero: '))
n=str(n)
n=n[:-1]
print(n)


'''
a = 13.946
print(a)
print("%.2f" % a)
print(round(a, 2))
print("%.2f" % round(a,2))
print("{0:.2f}".format(a))
print("{0:.2f}".format(round(a,2)))
print("{0:.15f}".format(round(a,2)))
'''

'''
def format_phone(self):
    # strip non-numeric characters
    phone = re.sub(r'\D', '', self.phone)
    # remove leading 1 (area codes never start with 1)
    phone = phone.lstrip('1')
    return '{}.{}.{}'.format(phone[0:3], phone[3:6], phone[6:])
'''