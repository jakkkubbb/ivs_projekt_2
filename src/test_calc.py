import unittest

from math_lib import *


class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(0,0),0)
        self.assertEqual(sum(10,5),15)
        self.assertEqual(sum(-1,2),1)
        self.assertEqual(sum(-1,-1),-2)
        self.assertEqual(sum(100,-100),0)
        self.assertEqual(sum(100000,100000),200000)
        x = 20
        y = 30 
        z = 50
        self.assertEqual(sum(x,y),z)
        self.assertEqual(sum(sum(x,y),z),x+y+z)
     
    def test_sum_float(self):
        self.assertEqual(sum(0.0,0.0),0.0)
        self.assertEqual(sum(10.5,5.5),16.0)
        self.assertEqual(sum(-1.5,2.5),1.0)
        self.assertEqual(sum(-1.5,-1.5),-3.0)
        self.assertEqual(sum(100.0,-100.0),0.0)
        self.assertEqual(sum(100000.5,100000.5),200001.0)
        x = 20.5
        y = 30.5 
        z = 51.0
        self.assertEqual(sum(x,y),z)
        self.assertEqual(sum(sum(x,y),z),x+y+z)

    def test_sub(self):
        self.assertEqual(sub(0,0),0)
        self.assertEqual(sub(10,5),5)
        self.assertEqual(sub(-1,2),-3)
        self.assertEqual(sub(-1,-1),0)
        self.assertEqual(sub(100,-100),200)
        self.assertEqual(sub(100000,100000),0)
        x = 20
        y = 30 
        z = -10
        self.assertEqual(sub(x,y),z)
        self.assertEqual(sub(sub(x,y),z),x-y-z)
    def test_sub_float(self):
        self.assertEqual(sub(0.0,0.0),0.0)
        self.assertEqual(sub(10.5,5.5),5.0)
        self.assertEqual(sub(-1.5,2.5),-4.0)
        self.assertEqual(sub(-1.5,-1.5),0.0)
        self.assertEqual(sub(100.0,-100.0),200.0)
        self.assertEqual(sub(100000.5,100000.5),0.0)
        x = 20.5
        y = 30.5
        z = -10.0
        self.assertEqual(sub(x,y),z)
        self.assertEqual(sub(sub(x,y),z),x-y-z)

    def test_mul(self):
        self.assertEqual(mul(0,0),0)
        self.assertEqual(mul(10,5),50)
        self.assertEqual(mul(-1,2),-2)
        self.assertEqual(mul(-1,-1),1)
        self.assertEqual(mul(100,-100),-10000)
        self.assertEqual(mul(100000,100000),10000000000)
        x = 20
        y = 30 
        z = 600
        self.assertEqual(mul(x,y),z)
        self.assertEqual(mul(x,y),mul(y,x))
        self.assertEqual(mul(mul(x,y),z),x*y*z)
    
    def test_mul_float(self):
        self.assertEqual(mul(0.0,0.0),0.0)
        self.assertEqual(mul(10.5,5.5),57.75)
        self.assertEqual(mul(-1.5,2.5),-3.75)
        self.assertEqual(mul(-1.5,-1.5),2.25)
        self.assertEqual(mul(100.0,-100.0),-10000.0)
        self.assertEqual(mul(100000.5,100000.5),10000100000.25)
        x = 20.5
        y = 30.5 
        z = 625.25
        self.assertEqual(mul(x,y),z)
        self.assertEqual(mul(x,y),mul(y,x))
        self.assertEqual(mul(mul(x,y),z),x*y*z)

    def test_div(self):
        self.assertEqual(div(0,1),0)
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(-1,2),-0.5)
        self.assertEqual(div(-1,-1),1)
        self.assertEqual(div(100,-100),-1)
        self.assertEqual(div(100000,100000),1)
        x = 20
        y = 4
        z = 5
        self.assertEqual(div(x,y),z)
        self.assertEqual(div(div(x,y),z),x/y/z)

    def test_div_float(self):
        self.assertEqual(div(0.0,1.0),0.0)
        self.assertEqual(div(4.5,2.0),2.25)
        self.assertEqual(div(-1.5,2.5),-0.6)
        self.assertEqual(div(-1.5,-1.5),1.0)
        self.assertEqual(div(100.0,-100.0),-1.0)
        self.assertEqual(div(100000.5,100000.5),1.0)
        x = 20.5
        y = 4.0
        z = 5.125
        self.assertEqual(div(x,y),z)
        self.assertEqual(div(div(x,y),z),x/y/z)
    
    def test_abs_v(self):
        self.assertEqual(abs_v(0),0)
        self.assertEqual(abs_v(10),10)
        self.assertEqual(abs_v(-1),1)
        self.assertEqual(abs_v(1),1)
        self.assertEqual(abs_v(100),100)
        self.assertEqual(abs_v(-100),100)
        x = -20
        y = 20
        self.assertEqual(abs_v(x),y)
        self.assertEqual(abs_v(x),abs_v(y))
    
    def test_abs_v_float(self):   
        self.assertEqual(abs_v(0.0),0.0)
        self.assertEqual(abs_v(10.5),10.5)
        self.assertEqual(abs_v(-1.5),1.5)
        self.assertEqual(abs_v(100.0),100.0)
        self.assertEqual(abs_v(-100.0),100.0)
        x = -20.5
        y = 20.5
        self.assertEqual(abs_v(x),y)
        self.assertEqual(abs_v(x),abs_v(y))

    def test_power(self):
        self.assertEqual(power(0,0),1)
        self.assertEqual(power(10,5),100000)
        self.assertEqual(power(-1,2),1)
        self.assertEqual(power(-1,-1),-1)
        self.assertEqual(power(100000,0),1)
        self.assertEqual(power(2,1),2)
        x = 20
        y = 2
        z = 400
        self.assertEqual(power(x,y),z)
        self.assertEqual(power(x,y),mul(x,x))

    def test_power_float(self):
        self.assertEqual(power(0.0,0.0),1.0)
        self.assertEqual(power(10.5,2.0),110.25)
        self.assertEqual(power(-1.5,2.0),2.25)
        self.assertEqual(power(4,0.5),2)
    
    
    def test_root(self):
        self.assertEqual(root(1,0),0)
        self.assertEqual(root(2,100),10)
        self.assertEqual(root(3,-1),"ERR")
        self.assertEqual(root(4,2),2)
        self.assertEqual(root(2,-1),"ERR")
        self.assertEqual(root(0,100000),"ERR")
        x = 400
        y = 2
        z = 20
        self.assertEqual(root(y,x),z)
        self.assertEqual(root(y,x),power(z,y))
    

    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5),120)

if __name__ == '__main__':
    unittest.main()