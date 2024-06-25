from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation= "vertical")
        self.solution = TextInput(background_color = "black",foreground_color = "white",
                                  multiline = False, halign="right", font_size=55, readonly= True)

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["DEL","="]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                if label == "=":
                    button.bind(on_press=self.on_solution)
                elif label == "DEL":
                    button.bind(on_press=self.on_delete)
                else:    
                    button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        
    def on_delete(self, instance):
        current = self.solution.text
        if current:
            self.solution.text = current[:-1]

    def on_solution(self, instance):
        text = self.solution.text
        try:
            if text:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
        except ZeroDivisionError:
            self.solution.text = "Error: Cannot Divide by Zero"
        except SyntaxError:
            self.solution.text = "Error: Invalid Expression"
        except NameError:
            self.solution.text = "Error: Invalid Variable"

if __name__ == "__main__":
    app = MainApp()
    app.run()