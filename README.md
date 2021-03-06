# Introduction
This is an application to analyze Caesar ciphers made using Streamlit.<br>
Download cc.py and run the following in a terminal.<br>
Then navigate to the local URL that appears.
```
$ streamlit run cc.py
```

# Description
The ciphertext should be generated at the link "Click here to generate ciphertext".<br>
Enter the Caesar ciphertext in the input field.<br>
For this example, we will enter the apple ciphertext "Dssoh".<br>
<img src="input.png">

The result will output 25 candidates as follows.<br>
There is always a cipher-decrypted plaintext among them.<br>
In this case, "Apple" is the correct answer, so the 23rd answer is correct.<br>
<img src="Apple.png">

# Postscript
In this case, we developed a simple Caesar cryptanalysis application using Streamlit.<br>
I found Streamlit very convenient and easy to use because I could write the program within a ".py file".<br>
I would like to add tools for analyzing other ciphers to this app in the future.<br>

Izuru Inose