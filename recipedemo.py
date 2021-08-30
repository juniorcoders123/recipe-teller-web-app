from py_edamam import Edamam
from PIL import Image
import streamlit as st
from io import BytesIO
import requests

st.title('Junior Coders Recipe Teller Web-App')
food = st.text_input("Enter the name of food for which you want recipe")

APP_ID = "5a8e712d"  # Put your app id for edamam api
APP_KEY = "bdc39ab5b9af47f619475bd78aa8985c"  # Put your app key for edamam api



if st.button("Get Recipe"):
    if food == '':
        st.warning("Food Criteria cannot be empty.")
    else:
        e = Edamam(recipes_appid=APP_ID, recipes_appkey=APP_KEY)
        dict = e.search_recipe(food)
        p = str(dict)
        if "image" not in p:
            st.subheader("No such food's recipe found")
            response = requests.get("https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg")
            img = Image.open(BytesIO(response.content))
            st.image(img)
        else:
            sl = p.split()


            def nextword(target, source):
                for i, w in enumerate(source):
                    if w == target:
                        return source[i + 1]


            imagelink = nextword("'image':", sl).replace("'", "")
            imagelink = imagelink.replace(",", "")
            recipelink = nextword("'shareAs':", sl).replace("'", "")
            recipelink = recipelink.replace(",", "")
            in1 = p.find('ingredientLines')
            in2 = p.find('ingredients')
            ingredientslist = p[in1:in2].replace("ingredientLines': [", "").replace("'", "").replace("],", ".").upper()
            st.subheader("Ingredients for Recipe :-")
            st.write(ingredientslist)
            st.subheader("Image of " + food)
            response = requests.get(imagelink)
            img = Image.open(BytesIO(response.content))
            st.image(img)
            st.markdown("Recipe Link :- " + recipelink, unsafe_allow_html=True)






