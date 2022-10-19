from copy import deepcopy
from sympy import symbols


def remove_forever_true_subset(input_list):
    '''
    预处理步骤，举例，当 input_list = [[a,~a]] 时
    此时[a, ~a]为永真式，故删除子式
    参数
        input_list: list[list[int]] :二维列表
    返回值
        None
    '''
    for i in input_list:
        for j in i:
            if ~j in i:
                input_list.remove(i)
                break


class Conjunctive:
    '''合取范式类'''
    def __init__(self, input_list):
        '''
        初始化函数
        参数
            input_list: list[list[int]] :二维列表
        返回值
            None
        '''
        self.conj = input_list

    def single_literal(self):
        '''
        找到范式中只含有一个字母的子集，举例
        self.conj = [[a], [~a, b]]
        则 [[a]] 就是我们要找的子集
        参数
            None
        返回值
            Symbol类 或 -1(表示不存在这样的子集)
        '''
        for i in self.conj:
            if len(i) == 1:
                return i[0]
        return -1

    def remove_true_subset(self, literal):
        '''
        删除所有含有literal的子集，以及删除所有含有~literal的字母
        参数
            literal: Symbol
        返回
            None
        '''
        for i in self.conj:
            if literal in i:
                self.conj.remove(i)
        for i in self.conj:
            if ~literal in i:
                i.remove(~literal)

    def output(self):
        '''
        对合取范式进行求值
        参数
            None
        返回
            True : 说明满足
            False: 说明出现矛盾
            -1   : 说明不确定
        '''
        if len(self.conj) == 0:
            return True
        elif [] in self.conj:
            return False
        return -1

    def search_nonvalue(self):
        '''
        找到下个没有被赋值的字母
        参数
            None
        返回
            Symbol
        '''
        return self.conj[0][0]


def dpll_algorithm(input_list):
    '''
    dpll算法，递归求解
    '''
    # 不断去掉合取范式中的单个字母
    while True:
        literal = input_list.single_literal()
        if literal == -1:
            break
        input_list.remove_true_subset(literal)
    # 求值
    ans = input_list.output() 
    if ans != -1:
        return ans
    literal = input_list.search_nonvalue()
    # 找到下一个没有被赋值的文字
    c_now = Conjunctive(deepcopy(input_list.conj))
    # 让这个文字取真
    c_now.remove_true_subset(literal)  
    if dpll_algorithm(c_now):
        return True
    c_now = Conjunctive(deepcopy(input_list.conj))
    # 让这个文字取假
    c_now.remove_true_subset(~literal) 
    if dpll_algorithm(c_now):
        return True
    return False


a, b, c, d, e = symbols('a b c d e')
l = [[~c], [~b], [d, e], [~a], [a, c]]
remove_forever_true_subset(l)
print(dpll_algorithm(Conjunctive(l)))

