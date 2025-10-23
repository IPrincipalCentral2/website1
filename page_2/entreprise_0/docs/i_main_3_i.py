












































































































list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["opencv-python"] ,
                            



]










import os


import traceback

import sys


import subprocess



print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])



try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
            
            
            #subprocess.check_call([sys.executable, "-m", "pip", "uninstall", f"{list_of_liberary_to_install[counter_0][0]}"])
            
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
import os
import shutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
)


class ImageFolderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📁 صنع مجلد بصورتين")
        self.setGeometry(300, 200, 650, 350)

        # ========== عناصر الواجهة ==========

        # الصورة 1
        self.image1_label = QLabel("الصورة 1:")
        self.image1_edit = QLineEdit()
        self.image1_edit.setPlaceholderText("أدخل مسار الصورة 1 أو اخترها...")
        self.image1_browse = QPushButton("📂 اختر")
        self.image1_browse.clicked.connect(lambda: self.browse_file(self.image1_edit))

        # الصورة 2
        self.image2_label = QLabel("الصورة 2:")
        self.image2_edit = QLineEdit()
        self.image2_edit.setPlaceholderText("أدخل مسار الصورة 2 أو اخترها...")
        self.image2_browse = QPushButton("📂 اختر")
        self.image2_browse.clicked.connect(lambda: self.browse_file(self.image2_edit))

        # اسم المجلد الجديد
        self.folder_name_label = QLabel("اسم المجلد الجديد:")
        self.folder_name_edit = QLineEdit()
        self.folder_name_edit.setPlaceholderText("اكتب اسم المجلد هنا...")

        # مكان إنشاء المجلد
        self.folder_path_label = QLabel("مكان حفظ المجلد:")
        self.folder_path_edit = QLineEdit()
        self.folder_path_edit.setPlaceholderText("اختر المكان الذي سيتم فيه إنشاء المجلد...")
        self.folder_path_browse = QPushButton("📁 اختر المجلد")
        self.folder_path_browse.clicked.connect(self.browse_folder_location)

        # زر الإنشاء
        self.create_button = QPushButton("🛠️ إنشاء المجلد ووضع الصور")
        self.create_button.clicked.connect(self.create_folder_with_images)

        # ========== تنظيم الواجهة ==========
        layout = QVBoxLayout()

        # صف الصورة 1
        row1 = QHBoxLayout()
        row1.addWidget(self.image1_label)
        row1.addWidget(self.image1_edit)
        row1.addWidget(self.image1_browse)

        # صف الصورة 2
        row2 = QHBoxLayout()
        row2.addWidget(self.image2_label)
        row2.addWidget(self.image2_edit)
        row2.addWidget(self.image2_browse)

        # صف مكان المجلد
        row3 = QHBoxLayout()
        row3.addWidget(self.folder_path_label)
        row3.addWidget(self.folder_path_edit)
        row3.addWidget(self.folder_path_browse)

        # تجميع الكل
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addWidget(self.folder_name_label)
        layout.addWidget(self.folder_name_edit)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    # ========== وظائف البرنامج ==========
    def browse_file(self, line_edit):
        file_path, _ = QFileDialog.getOpenFileName(self, "اختر صورة", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            line_edit.setText(file_path)

    def browse_folder_location(self):
        folder_path = QFileDialog.getExistingDirectory(self, "اختر مكان إنشاء المجلد")
        if folder_path:
            self.folder_path_edit.setText(folder_path)

    def create_folder_with_images(self):
        img1 = self.image1_edit.text().strip()
        img2 = self.image2_edit.text().strip()
        folder_name = self.folder_name_edit.text().strip()
        base_path = self.folder_path_edit.text().strip()

        # تحقق من الحقول
        if not img1 or not img2 or not folder_name or not base_path:
            QMessageBox.warning(self, "⚠️ خطأ", "يرجى إدخال جميع الحقول أو اختيار الصور والمجلد.")
            return

        # المسار الكامل للمجلد الجديد
        folder_path = os.path.join(base_path, folder_name)

        # إنشاء المجلد
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # نسخ الصور إليه
            shutil.copy(img1, os.path.join(folder_path, os.path.basename(img1)))
            shutil.copy(img2, os.path.join(folder_path, os.path.basename(img2)))

            QMessageBox.information(
                self, "✅ تم بنجاح",
                f"تم إنشاء المجلد:\n{folder_path}\n\nوتم وضع الصورتين بداخله."
            )
        except Exception as e:
            QMessageBox.critical(self, "❌ خطأ", f"حدث خطأ أثناء إنشاء المجلد:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFolderApp()
    window.show()
    sys.exit(app.exec_())



















