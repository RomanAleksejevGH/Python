mylist = ['abc123','abc321', 'def456', 'ghi789', 'ABC 987', 'aBc654']
sub = 'abc'

print ("\n".join(s for s in mylist if sub.lower() in s.lower()))
