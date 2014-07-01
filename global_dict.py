######### global_dict class
import operator as op
import math

class global_dict:
    env={}
    def __init__(self):
        env.update(vars(math))
        env.update(
            {'+':op.add,
             '-':op.sub
             '*':op.mul
             '/':op/div
             'not':op.not_
             '>':op.gt
             '<':op.lt
             '>=':op.ge
             '<=':op.le
             '=':op.eq
             'equal?':op.eq
             'eq?':op.is_
             'length':len
             'cons':lambda x,y:[x]+y
