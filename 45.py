a=input()

a=a.replace('&gt;','>')
a=a.replace('&quot;','"')
a=a.replace('&apos;',"'")
a=a.replace('&lt;','<')
a=a.replace('&frasl;','/')
a=a.replace('&amp;','&')


print(a)