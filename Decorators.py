'''def fun():
    print("Decorators in python.")
fun2=fun
del fun
fun2()

'''

"""def fruits(clr):
    if clr=='red':
        return 'apple'

    if clr=="yellow":
        return 'banana'

f=fruits('red')
print(f)
"""


"""
def outFUN(inFUN):
    inFUN("this is inner fun.")
outFUN(print)
#print(outFUN)

def exe(fun):
     fun("fun funcion")
exe(print)
"""


def dec1(fun):
    def exec():
        print("executing")
        fun()
        print("executed")
    return  exec()
@dec1
def python():
    print("python")

#py=dec1(python)

#python()



