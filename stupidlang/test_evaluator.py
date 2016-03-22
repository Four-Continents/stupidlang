import unittest
from .evaluator import global_env, eval_ptree
from .env_dictimpl import Env
from .parser import parse
    
class EvaluatorTests(unittest.TestCase):
    
    def test_global_env(self):
        # test return type
        self.assertTrue( str(type(global_env(Env))) == "<class 'stupidlang.env_dictimpl.Env'>" )
        # test existence of a specific operator
        self.assertTrue( str(global_env(Env).lookup("*")[0]) == "<built-in function mul>" )
        
    def test_eval_ptree(self):
        env=global_env(Env)
        # test simple expression
        self.assertTrue( eval_ptree(parse('(- (+ 1 7) 2)'), env) == 6 )
        # test expression with booleans
        self.assertTrue( eval_ptree(parse("(+ true (+ 2 (* 3 false)))"), env) == 3 )
        # test noop
        self.assertTrue( eval_ptree([], env) == None )
        # test conditionals
        self.assertTrue( eval_ptree(parse("(if (== 3 2) true false)"), env)  == False )
        # test function
        self.assertTrue( eval_ptree(parse("(func x (+ x 1))"), env)(5) == 6 )
        

if __name__ == '__main__':
    unittest.main()
