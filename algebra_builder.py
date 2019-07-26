from IPython.display import display, Markdown
import random
from collections import Counter
from IPython.display import HTML
def toggle_button():
    # Hide from print preview use $('div.input').html("")
    HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
class Simplification():
    def __init__(self):
        self.samples = []

    @classmethod
    def type1(cls):
        a = random.randint(1,9)
        b = random.randint(2,9)
        return a*a*b

    @classmethod
    def type2(cls):
        a = random.randint(1,9)
        b = random.randint(2,5)
        c = random.randint(2,5)
        return a*a*b*c

    @classmethod
    def type12(cls):
        c = random.randint(0,1)
        if c:
            return cls.type1()
        else:
            return cls.type2()

    @classmethod
    def simple_prime_factorization(cls, num):
        def _iter_(x,y):
            if x==1:
                return y
            for each in [2,3,5,7,11,13,17,19]:
                if x % each == 0:
                    y.append(each)
                    return _iter_(int(x/each), y)

        return _iter_(num, [])

    @classmethod
    def simplify_sqrt(cls, num):
        a=1
        b=1
        for k,v  in Counter(cls.simple_prime_factorization(num)).items():
            a *= k**int(v/2)
            if v%2:
                b *= k
        return a,b

class BasicSimplification(Simplification):
    
    def generate(self, n):
        samples = []

        while len(samples)<n:
            x = self.type12()
            if not x in samples:
                samples.append(self.type12())
        self.samples=samples

    def output_exercises(self):
        display(Markdown('#### Exercises ####'))
        count = 0
        for each in self.samples:
            count +=1
            display(Markdown('{}) $\sqrt{{{}}}$'.format(count, each)))
    
    def output_solutions(self):
        display(Markdown('#### Solutions ####'))
        count = 0
        for each in self.samples:
            count +=1
            display(Markdown('{}) $\sqrt{{{}}}={}$'.format(count, each, self.display_simplified(each))))

    def display_simplified(self, num):
        a,b = self.simplify_sqrt(num)
        da = ''
        db=''
        if a>1:
            da = '{}'.format(a)
        if b>1:

            db='\sqrt{{{}}}'.format(b)
        return da+db
from math import gcd
class QuotientSimplification(Simplification):
    
    def generate(self, n):
        samples = []
        
        while len(samples)<n:    
            numerator = random.randint(1, 9)*random.randint(1,9)
            x=(numerator, self.type12())
            if not x in samples:
                samples.append(x)
        self.samples=samples

    def output_exercises(self):
        display(Markdown('#### Exercises ####'))
        count = 0
        for each in self.samples:
            count +=1
            display(Markdown('{}) $\displaystyle {{{}\over\sqrt{{{}}}}}$'.format(count, each[0],each[1])))

    def output_solutions(self):
        display(Markdown('#### Solutions ####'))
        count = 0
        for each in self.samples:
            count +=1
            display(Markdown('{}) $\displaystyle {{{}\over\sqrt{{{}}}}}={}$'.format(count, each[0],each[1],self.display_simplified(each))))

    def display_simplified(self, quot):
        num, denom = quot
        a1,b = self.simplify_sqrt(denom)
        a=num
        c=a1*b
        gc = gcd(c,num)
        a=int(a/gc)
        c=int(c/gc)
        da = ''
        db=''
        if a>1:
            da = '{}'.format(a)
        if b>1:
            db='\sqrt{{{}}}'.format(b)
        if c>1:
            return '{{{}\over{}}}'.format(da+db,c)
        return da+db
"""    
from sympy import sqrt as simsqrt
from sympy import latex, simplify
class MixedSimplification(Simplification):
    def generate(self, n):
        samples = []
        while len(samples)<n:
            a = random.randint(-9,9)
            b= random.choice([-5,-4,-3, -2, -1, 1, 2,3,4,5])
            c= random.randint(-9,9)
            d= random.choice([-5,-4,-3, -2, -1, 1, 2,3,4,5])
            e = random.choice([2,3,5,6,7,8,10])
            x=(a,b,c,d,e)
            if not x in samples:
                samples.append(x)
        self.samples=samples
    
    def output_exercises(self):
        display(Markdown('#### Exercises ####'))
        count = 0
        for a,b,c,d,e in self.samples:
            count +=1
            display(Markdown('{}) $\displaystyle {}$'.format(count, latex((a+b*simsqrt(e))*(c+d*simsqrt(e)))))  )  

    def output_solutions(self):
        display(Markdown('#### Solutions ####'))
        count = 0
        for a,b,c,d,e in self.samples:
            count +=1
            eq = (a+b*simsqrt(e))*(c+d*simsqrt(e))
            display(Markdown('{}) $\displaystyle {}={}$'.format(count, latex(eq), latex(simplify(eq)))))   
            
"""            
def root(a,b):
    if a==1:
        return b
    if a==2:
        return r'{{\sqrt{{{}}}}}'.format(b)
    else:
            return r'{{\root {} \of {{{}}}}}'.format(a,b)
#            return r'{{\root {} \of {}}}'.format(a,b)

class RadicalSimplification(Simplification):
    def generate(self, n):
        samples = []
        while len(samples)<n:
            a = random.randint(2,9)
            b= random.randint(2,a)
            c= random.randint(1,3)
            d= random.randint(2,10)
            x=[a,b,c,d]
            random.shuffle(x[0:2])
            if not x in samples:
                samples.append(x)
        self.samples=samples
    
    def output_exercises(self):
        display(Markdown('#### Exercises ####'))
        count = 0
        for x in self.samples:
            count +=1
            display(Markdown('{}) $\displaystyle {}$'.format(count, root(x[0],root(x[1], root(x[2],x[3]))))))

    def output_solutions(self):
        display(Markdown('#### Solutions ####'))
        count = 0
        for a,b,c,d in self.samples:
            expr = root(a,root(b, root(c,d)))
            rad = a*b*c
            if d==4 and rad%2==0:
                rad=int(rad/2)
                d=2
            if d==9 and rad%2==0:
                rad=int(rad/2)
                d=3
            if d==8 and rad %3==0:
                rad= int(rad/3)
                d=2
            count+=1
            display(Markdown('{}) $\displaystyle {}={}$'.format(count, expr, root(rad,d))))
# document.querySelectorAll("div.input").forEach(function(a){a.remove()})
