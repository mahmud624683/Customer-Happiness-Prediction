import subprocess
print("<==================install pandas================>")
bashCommand = "pip3 install pandas"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode("utf-8"))
print("<==================install numpy================>")
bashCommand = "pip3 install numpy"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode("utf-8"))

print("<==================install scikit learn================>")
bashCommand = "pip3 install sklearn"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode("utf-8"))

print("<==================install nltk packages================>")
bashCommand = "pip3 install nltk"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode("utf-8"))
import nltk
nltk.download()