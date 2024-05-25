import streamlit as st

st.title("Welcome to Tahaa's Calculator")
# st.markdown("## Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
options = st.radio(
    "Enter the operation you want to perform",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)
if options == "Addition":
    ans = num1 + num2

elif options == "Subtraction":
    ans = num1 - num2

elif options == "Multiplication":
    ans = num1 * num2

elif options == "Division":
    ans = num1 / num2
    if num2 == 0:
        st.text("Cannot divide by Zero")

if st.button("Calculate", type="primary"):
    st.success("Your Answer is {}.".format(ans))


