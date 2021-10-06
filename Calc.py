from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

#App size
Window.size = (500,700)

Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
   #Button Creating function 
    def button_press(self, button):
    #variable creating
        prior = self.ids.calc_input.text

        #Error test
        if "Error" in prior:
            prior = ''

    #determine 0 is there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
         self.ids.calc_input.text = f'{prior}{button}'

            #add function
    def math_sign(self, sign):
        #variable creating
        prior = self.ids.calc_input.text
        #plus sign to text box
        self.ids.calc_input.text = f'{prior}{sign}'        
            
        
        #function to remove the last character
    def remove(self):   
        prior = self.ids.calc_input.text 
        #remove the last item inn the text box
        prior = prior [:-1]
        #output
        self.ids.calc_input.text = prior

    #create function for postive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text 
        #to see there is a -sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}' 
        else:
            self.ids.calc_input.text = f'-{prior}'  


        #decimal function   
    def dot(self):
        prior = self.ids.calc_input.text 
        #Split out
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior   
        
        
        elif "." in prior:
                pass        
        else:
                prior = f'{prior}.'
                self.ids.calc_input.text = prior
       
        
   #create equals sign 
    def equals(self):
        prior = self.ids.calc_input.text
        #error
        try:
            #Evaluate math from text box
            answer = eval(prior)

        #Output
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
    
    
    '''
    #Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            #loop
            for number in num_list:
                answer = answer + float(number)
            #print the ans
            self.ids.calc_input.text = str(answer)
       ''' 
        
class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    
    CalculatorApp().run()


