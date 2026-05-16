#Assignment on funvtion in the list class
thislist=["banana","apple","grape","watermelon","orange"]
#thislist.clear()
print(thislist)# output=[]
thislist.append("qiwi")
print(thislist)#['banana', 'apple', 'grape', 'watermelon', 'orange', 'qiwi']
newlist=thislist.copy()
print(newlist)#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'qiwi']
print(thislist.count("apple"))#output=1
thislist.extend(["mango", "pineapple"])
print(thislist)#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'qiwi', 'mango', 'pineapple']
print(thislist.index("grape"))#output=2
thislist.insert(2, "cherry")
print(thislist)#['banana', 'apple', 'cherry', 'grape', 'watermelon', 'orange', 'qiwi', 'mango', 'pineapple']
thislist.pop()
print(thislist)#output=['banana', 'apple', 'cherry', 'grape', 'watermelon', 'orange', 'qiwi', 'mango']
thislist.remove("apple")
print(thislist)#output=['banana', 'grape', 'watermelon', 'orange', 'qiwi', 'mango']
thislist.reverse()
print(thislist)#output=['mango', 'qiwi', 'orange', 'watermelon', 'grape', 'banana']
thislist.sort()
print(thislist)#output=['banana', 'grape', 'mango', 'orange', 'qiwi', 'watermelon']
Alist= thislist.__add__(["raspberry", "blueberry"])
print(Alist)#['banana', 'cherry', 'grape', 'mango', 'orange', 'qiwi', 'watermelon', 'raspberry', 'blueberry']
__annotations__ = {"thislist": "list of strings"}
print(__annotations__)#output={'thislist': 'list of strings'}


thislist=["banana","apple","grape","watermelon","orange"]

print(thislist.__class__)#output=<class 'list'>
print(list.__class_getitem__(int))#output=typing.List[int]
print(thislist.__contains__("banana"))#output=True
thislist.__delitem__(1)
print(thislist)#output=['banana', 'grape', 'watermelon', 'orange']
print(thislist.__class__)#output=<class 'list'>
print(thislist.__dir__())#output=list of attributes
print(thislist.__doc__)#output=Built-in mutable sequence.
print(thislist.__eq__(["banana","grape","watermelon","orange"]))#output=True
print(thislist.__ge__(["apple"]))#output=True or False depending on comparison rules
print(thislist.__getitem__(2))#output=grape
print(format(thislist))#output=['banana', 'apple', 'grape', 'watermelon', 'orange']
print(thislist.__getattribute__("append"))#output=<built-in method append of list object>
print(getattr(thislist, "__getstate__", None))#output=None
print(thislist.__gt__(["apple"]))#output=True or False depending on comparison rules
thislist=["banana","apple","grape","watermelon","orange"]
print(thislist.__hash__)#output=None
thislist.__iadd__(["mango"])
print(thislist)#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'mango']
thislist.__imul__(2)
print(thislist)#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'mango', 'banana', 'apple', 'grape', 'watermelon', 'orange', 'mango']
thislist.__init__(["kiwi","pear"])
print(thislist)#output=['kiwi', 'pear']
print(type(thislist).__init_subclass__)#output=<function __init_subclass__ at ...>
it = thislist.__iter__()
print(next(it))#output=banana
print(thislist.__le__(["zebra"]))#output=True or False depending on comparison
print(thislist.__len__())#output=5thislist=["banana","apple","grape","watermelon","orange"]
print(type(thislist).__module__)#output=builtins
print(thislist.__mul__(2))#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'banana', 'apple', 'grape', 'watermelon', 'orange']
print(thislist.__ne__(["apple","banana"]))#output=True
print(list.__new__(list))#output=[]
print(list.__qualname__)#output=list
print(thislist.__lt__(["zebra"]))#output=True or False depending on comparison


thislist=["banana","apple","grape","watermelon","orange"]

print(thislist.__repr__())#output="['banana', 'apple', 'grape', 'watermelon', 'orange']"
print(list(thislist.__reversed__()))#output=['orange', 'watermelon', 'grape', 'apple', 'banana']
print(thislist.__rmul__(2))#output=['banana', 'apple', 'grape', 'watermelon', 'orange', 'banana', 'apple', 'grape', 'watermelon', 'orange']
thislist=["banana","apple","grape","watermelon","orange"]
thislist.__setitem__(1, "kiwi")
print(thislist)#output=['banana', 'kiwi', 'grape', 'watermelon', 'orange']
print(thislist.__sizeof__())#output=memory size (varies, e.g. 104)
print(thislist.__str__())#output="['banana', 'kiwi', 'grape', 'watermelon', 'orange']"
print(list.__subclasshook__)#output=<built-in method __subclasshook__ of type object>