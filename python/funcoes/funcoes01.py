# concat('abc', 'def') => 'abcdef'
# concat('abc', 23, True, ['alberto', 19]) => "abc23True['alberto', 19]"
# concat('abc', 23, 'def', sep='/', end='.') => 'abc/23/def.'

def concat(*args):
    item_str = []
    for arg in args:
        item_str.append(str(arg))
    
    return ''.join(item_str)




















