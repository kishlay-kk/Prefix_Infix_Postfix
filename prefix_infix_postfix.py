#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division
import random


# In[2]:


OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}                      #DEFINING THE  OPERATORS USED 


# In[57]:


def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop();
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop();
            stack.append(ch)
    # leftover
    while stack: output += stack.pop();
    #print (output)
    return output


# In[6]:


def postfix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in formula:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop();
            a = stack.pop();
            if prev_op and len(a) > 1 and PRIORITY[ch] > PRIORITY[prev_op]:
                # if previous operator has lower priority
                # add '()' to the previous a
                expr = '('+a+')' + ch + b
            else:
                expr = a + ch + b
            stack.append(expr)
            prev_op = ch
    #print (stack[-1])
    #return stack[-1]


# In[7]:


def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print (exp_stack[-1])
    return exp_stack[-1]


# In[8]:


def prefix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in reversed(formula):
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if prev_op and PRIORITY[prev_op] < PRIORITY[ch]:
                exp = '('+a+')'+ch+b
            else:
                exp = a+ch+b
            stack.append(exp)
            prev_op = ch
    print (stack[-1])
    return stack[-1]


# In[62]:


s1=infix_to_postfix('1+(3+4*6+6*1)*2/3')
s2=infix_to_prefix('1+(3+4*6+6*1)*2/3')
s3=postfix_to_infix('1346*+61*+2*3/+')
s4=prefix_to_infix('+1/*++3*46*6123')


# In[ ]:




