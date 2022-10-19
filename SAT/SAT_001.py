from copy import deepcopy
from sympy import symbols


def remove_forever_true_subset(input_list):
    for i in input_list:
        for j in i:
            if ~j in i:
                input_list.remove(i)  # x | ~x等价于1，删除该子句
                break


class Conjunctive:  # 合取范式类
    def __init__(self, input_list):
        # l: 集合的列表，里面的集合是子句，外面的列表是CNF
        self.conj = input_list

    def single_literal(self):  # 找到单位子句
        for i in self.conj:
            if len(i) == 1:
                return i[0]  # 返回单位子句含有的文字
        return -1  # 找不到，返回None

    def remove_true_subset(self, literal):
        # 以文字literal对cnf进行单位传播
        for i in self.conj:  # 需要拷贝self.cnf
            if literal in i:  # 含有literal的子句直接删除
                self.conj.remove(i)
        for i in self.conj:
            if ~literal in i:
                i.remove(~literal)  # 删除literal的否定

    def output(self):  # 对CNF求值
        if len(self.conj) == 0:  # CNF为空，可满足
            return True
        elif [] in self.conj:  # CNF含有空子句，不满足（出现矛盾）
            return False
        return -1  # 无法确定，返回None

    def search_nonvalue(self):  # 找到下一个没有被赋值的文字
        return self.conj[0][0]  # 直接返回第一个子句的第一个文字


def DPLL(c):
    while True:  # 不断使用单位传播，直到没有单位子句为止
        literal = c.single_literal()  # 找到单位子句包含的文字
        if literal == -1:  # 无单位子句，退出循环
            break
        c.remove_true_subset(literal)  # 执行单位传播
    ans = c.output()  # 求值
    if ans != -1:
        return ans
    literal = c.search_nonvalue()
    # 找到下一个没有被赋值的文字
    c_now = Conjunctive(deepcopy(c.conj))
    c_now.remove_true_subset(literal)  # 让这个文字取真
    if DPLL(c_now):
        return True
    c_now = Conjunctive(deepcopy(c.conj))
    c_now.remove_true_subset(~literal)  # 让这个文字取假
    if DPLL(c_now):
        return True
    return False


a, b, c, d, e = symbols('a b c d e')
l = [[~c], [~b], [d, e], [~a], [a, c]]
remove_forever_true_subset(l)
print(DPLL(Conjunctive(l)))

