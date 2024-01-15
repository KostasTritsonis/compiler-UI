from PyQt6.QtCore import QProcess
import FactoryMethod,subprocess

def runIntermidiate(self):
    self.process = QProcess()
    scriptPath  = "python {compiler} {currentPath}".format(currentPath=self.path,compiler=self.compiler)
    self.process.startCommand(scriptPath)
    if(self.process.waitForFinished() == False):
        return
    output = self.process.readAllStandardOutput().data().decode()
    self.output = output
    error = self.process.exitCode()
    if error == 1:
        FactoryMethod.command(self,'error')  
    else:
        output = self.setOutput(output)
        self.textEdit.setText(output)
        self.show()
        
def runFinal(self):
    scriptPath  = "python -u {compiler} None".format(compiler=self.path)
    self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    finalTtext = ''
    while self.process.poll() is None:
        line = self.process.stdout.readline().strip()
        if line:
            if 'Give input' in line:
                self.line = line
                self.giveInput()
                self.process.stdin.write(self.inputValue + "\n")
                self.process.stdin.flush()
            else:
                finalTtext+=line+'\n'
        self.textEdit.setText(finalTtext)
    self.process.stdin.close()
    
def runDebug(self):
    scriptPath  = "python -u {compiler} {line}".format(compiler=self.path,line=self.breakPoint)
    self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    finalText = ''
    while self.process.poll() is None:
        line = self.process.stdout.readline().strip()
        if line:
            if 'Give input' in line:
                self.line = line
                self.giveInput()
                self.process.stdin.write(self.inputValue + "\n")
                self.process.stdin.flush()
            if line == '-':
                while self.process.poll() is None:
                    line = self.process.stdout.readline().strip()
                    finalText+=line+'\n'
    self.textEdit.setText(finalText.strip())
    self.process.stdin.close()