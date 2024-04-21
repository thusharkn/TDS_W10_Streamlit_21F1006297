import streamlit as st

st.title("Find the largest among three given numbers")
st.write("Enter the numbers:")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)
c = st.number_input("Enter third number", value=0)

    if st.button("Find Largest"):
        largest = max(a, b, c)
        st.write(f"The largest number is: {largest}")

if __name__ == "_main_":
    main()
