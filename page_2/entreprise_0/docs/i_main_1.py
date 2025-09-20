















list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess





try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
        
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    


print("\n" * 10)





import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("فتح رابط بالمتصفح")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        # Label
        self.label = QLabel("اضغط على الزر لفتح الرابط:", self)
        layout.addWidget(self.label)

        # Button
        self.button = QPushButton("فتح الرابط", self)
        self.button.clicked.connect(self.open_link)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_link(self):
        
                
        # ضع الرابط الذي تريده هنا
        
        
        url = "https://iprincipalcentral2.github.io/website1/page_2/entreprise_0/i_page_of_interface_1_i.html"
        
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())















