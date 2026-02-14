import streamlit as st

# todo: The Automated "Math-to-LaTeX" Converter
# todo: Writing lab reports or assignments in LaTeX can be a chore. Built a tool that takes "lazy" mathematical shorthand and converts it into clean LaTeX code.
# - How it works: Used input() to take a string like sum from 1 to n of x^2.
# - The Logic: Used .replace() and .split() to turn "sum from" into \sum_{...}^{...} and x^2 into x^{2}.
# - Why it helps: It reinforces your understanding of string parsing and provides a genuine utility for your classmates' documentation.

st.title('🎓 Math to LaTeX Converter')
st.write('Type your equation in plain English')
MathSum = st.text_input('Enter an Equation:', placeholder='e.g., 2 raise to x+3 sum from 1 to 10, root 400, 5 over 10, x+5 / 5-y')

# splits MathSum into lists
parts = MathSum.split()

# displays result only if user enters input field
if MathSum:
    # checks if sum from is in user's input
    if 'from' in MathSum:
        numerator = MathSum.split('from')[1].split('to')[0].strip() # strip() ensure there are no spaces in LaTeX Output e.g., \sum_{ 1 }^{ n }
        denominator = parts[parts.index('to') + 1].strip()
        # prints numerator and denominator in LaTeX format
        result = rf'\sum_{{{numerator}}}^{{{denominator}}}'

    elif 'over' in parts or '/' in parts:
        if 'over' in parts:
            parts =MathSum.split('over')
        else:
            parts = MathSum.split('/')
        numerator = parts[0].strip()
        denominator = parts[1].strip()
        # prints output in LaTeX format 
        result = rf'\frac{{{numerator}}}{{{denominator}}}'

    elif 'root' in parts:
        root_value = MathSum.split('root')[1].strip()
        # prints result in LaTeX format
        result = rf'\sqrt{{{root_value}}}'
    
    elif 'pi' in parts:
        pi = MathSum.replace('pi', r'\pi').strip()
        # prints result in LaTeX format
        result = rf'{{{pi}}}'

    elif 'theta' in parts:
        theta = MathSum.replace('theta', r'\theta').strip()
        # print result in LaTeX format
        result = rf'{{{theta}}}'

    elif 'alpha' in parts:
        alpha = MathSum.replace('alpha', r'\alpha')
        # print result in LaTeX format
        result = rf'{{{alpha}}}'

    elif 'beta' in parts:
        beta = MathSum.replace('beta', r'\beta')
        # print result in LaTeX format
        result = rf'{{{beta}}}'
        
    elif 'gamma' in parts:
        gamma = MathSum.replace('gamma', r'\gamma')
        # print result in LaTeX format
        result = rf'{{{gamma}}}'
        
    elif 'raise' in parts:
        num = MathSum.split('raise')[0].strip()
        power = MathSum.split('to')[1].strip()
        
        # print result in LaTeX format
        result = rf'{{{num}}}^{{{power}}}'

    else:
        result = 'Operation not yet recognized!'
        
    # -- The output
    st.subheader("LaTeX Output:")
    st.code(result)

    st.subheader("Mathematical Preview:")
    st.latex(result)