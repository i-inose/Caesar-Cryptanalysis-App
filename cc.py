# シーザー暗号解析プログラム
import streamlit as st
from cProfile import label


def decode(str, key):
	plaintext = ""

	for i in list(str):
		if "A" <= i <= "Z":
			plaintext += chr((ord(i) - ord("A") + key) % 26 + ord("A"))
		elif "a" <= i <= "z":
			plaintext += chr((ord(i) -ord("a") + key) % 26 + ord("a"))
		else:
			plaintext += i
	return plaintext

if __name__ == "__main__":
	st.title("シーザー暗号解析")
	st.subheader("シーザー暗号を解析します。")
	link = "[暗号文生成はこちら](https://linesegment.web.fc2.com/application/cipher/Caesar.html)"
	st.write(link, unsafe_allow_html=True)
	ciphertext = st.text_input(label="シーザー暗号文を入力してください。")
	st.caption("入力された暗号文 : " + ciphertext)
	for j in range(1, 26):
		st.write("解析結果候補 {0:2d}".format(j) + " : " + decode(ciphertext, j))