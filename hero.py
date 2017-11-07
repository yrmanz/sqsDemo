#! /usr/bin/python
__author__="Manjunatha YR"

import unittest
from   selenium                                      import  webdriver
from   selenium.webdriver.support.wait               import  WebDriverWait 
from   selenium.webdriver.support.select             import  Select
from   selenium.webdriver.support                    import  expected_conditions as EC 
from   selenium.webdriver.common.action_chains       import  ActionChains
from   selenium.webdriver.common.by                  import  By 
from   browserAndUrl1                                import  Cons
from   guiOperations1                                import  operation
import time
import re



class sqsLogin(unittest.TestCase, Cons, operation):
    '''
    1.Invoke browser 2.enter the url 3.Maximize window.
    '''
    
     
    def setUp(self):
        global driver
        a=Cons('herokuapp','Firefox')
        b=a.funcConstants()
        driver=super(sqsLogin,self).InvokeBrowserAndMaximize(b[0],b[1])
       
        
        
    def testCase1_assertPage(self): 
        '''
        1.Obtain all the GUI elements objests of Login Screen. 
        2.Assert for appropriate web page.
        '''
        global pageElementObject,button1,button2,button3,edit1,edit2,edit3,edit4,edit5,edit6,edit7,edit8,edit9,edit10,delete1,delete2,delete3,delete4,delete5,delete6,delete7,delete8,delete9,delete10,answerElement,cdom
        
        csvFilePath             = super(sqsLogin, self).filePath("sqsDemo1.csv")
        pageElementObject       = super(sqsLogin, self).elePageObj(csvFilePath)
        
        #Invoke the SQSDemo homepage and assert the home page.
        pan1=driver.title
        self.assertEqual(driver.title, u'The Internet')

    def testCase2_checkText(self): 
        '''
        GUI element text check.
        
        '''
        dom = pageElementObject['cdom']
        dom = eval(dom) 
        domText=dom.text
        print "domText",domText
        try:
            self.assertEqual(domText,"Challenging DOM")
        except:
            print "Assert Error!"


    def testCase3_GuiStandardization(self):
        '''
        GUI Standardization test of the web elements.
        '''
        button1 = eval(pageElementObject['button1'])
        button2 = eval(pageElementObject['button2'])
        button3 = eval(pageElementObject['button3'])
        edit1   = eval(pageElementObject['edit1'])
        edit2   = eval(pageElementObject['edit2'])
               
        # Default GUI elements properties    
        try:
           self.assertTrue(button1.is_displayed())
        except:
            print "button not displyed"
        try:
           self.assertTrue(button2.is_displayed())
        except:
            print "button2 not displayed"
        try:
           self.assertTrue(button3.is_displayed())
        except:
            print "button3 is not displayed"
        try:     
            self.assertTrue(button1.is_enabled())
        except:
            print "button1 is not enabled"
        try:
            self.assertTrue(button2.is_enabled())
        except:
            print "button2 is not enabled"
             
        try:
            self.assertTrue(edit1.is_enabled())
        except:
            print "edit1 is not enabled"

        try:
            self.assertTrue(edit2.is_enabled())
        except:
            print "edit1 is not enabled"
      
    

    def testCase4_GitHubLink(self):
        '''
        check for the GITHUB link.
        '''


        clickForkMe=eval(pageElementObject["clickForkMe"])
        clickForkMe.click()
        pan2=driver.title
        regExp=re.compile(r'GitHub$')
        try:
            regExp.match(pan2)
        except:
            print "not expexted webpage"     
        
        driver.back()


    def testcase5_ElementSelenium(self):
        '''
        Check for selenium elemental link.
        '''
        linkSelenium = eval(pageElementObject["linkSelenium"])
        linkSelenium.click()
        title="The Internet"
        pan3 =driver.title
        print "pan3", pan3 
        try:
            self.assertEqual(pan3,title) 
        except:
            print "not expexted webpage"    
        driver.back()
      
    
    def testCase6_blueButton(self):
        '''
        Check for the blue button behaviour
        '''


        button1     = eval(pageElementObject['button1']) 
        text1       = button1.text
        print 'text1',text1
        button1.click()
        button1     = eval(pageElementObject['button1']) 
        text2       = button1.text
        print "text2", text2
        
        try:
            self.assertNotEqual(text1,text2)
        except:
            print "button text should have been changed" 
        
                 
    def testCase7_redButton(self):
        '''
        Check for the red button behaviour
        '''
        button2     = eval(pageElementObject['button2'])     
        text1       = button2.text
        print 'text1',text1
        button2.click()
        button2     = eval(pageElementObject['button2']) 
        text2       = button2.text
        print "text2", text2
        
        try:
            self.assertNotEqual(text1,text2)
        except:
            print "button text should have been changed" 
    

    def testCase8_greenButton(self):
        '''                                       
        Check for the green button behaviour
        '''
 

        button3    = eval(pageElementObject['button3'])     
        text1      = button3.text
        print 'text1',text1
        button3.click()
        button2     = eval(pageElementObject['button2']) 
        text2       = button2.text
        print "text2", text2
        try:
            self.assertNotEqual(text1,text2)
        except:
            print "button text should have been changed"


    def testCase9_linkedit(self):
        '''
        check for the LINK 
        '''
        edit1 = eval(pageElementObject['edit1']) 
        edit1.click()                                
        try:
            edit1.click() 
            driver.switch_to_frame("del_frame_elm")
        except:
            print "edit frame failed to pop up"
 
   
    def testCase10_linkdelete(self):
        '''
         check for delete liink behaviour 
        '''
        csvFilePath             = super(sqsLogin, self).filePath("sqsDemo1.csv")
        pageElementObject       = super(sqsLogin, self).elePageObj(csvFilePath)
        delete1 = eval(pageElementObject['delete1']) 
        delete1.click()                                
        try:
            delete1.click() 
            driver.switch_to_frame("del_frame_elm")
        except:
            print "delete frame failed to pop up"
 
    def tearDown(self):
        driver.close()
               
if __name__ == "__main__":
    unittest.main()
