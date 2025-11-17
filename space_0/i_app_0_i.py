









































































































list_of_liberary_to_install = [
                            
                            
                            ["flask"] ,
                            
                            


]










import os


import traceback

import sys


import subprocess




cwd = os.path.dirname(os.path.abspath(__file__))



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









from flask import Flask, send_from_directory, jsonify
import os
import json

app = Flask(__name__, static_folder="static")

# تقديم أي HTML موجود في نفس المجلد
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# تقديم أي ملف HTML آخر
@app.route("/<path:filename>")
def serve_file(filename):
    # إذا كان طلب JSON:
    if filename.endswith(".json"):
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({"error": "JSON file not found"}), 404

    # إذا كان طلب HTML/CSS/JS/PNG/...:
    if os.path.exists(filename):
        return send_from_directory(".", filename)

    return "File Not Found", 404


if __name__ == "__main__":
    app.run(debug=True)












