from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from helpers import screen_helper
import pandas as pd
from food_recommender import give_rec
from kivymd.uix.list import ThreeLineListItem
import pickle

DATAFILE = 'users.pickle.txt'
USERS = {}

Window.size = (358, 600)
df = pd.read_csv(r"indian_food.csv")
df_cleaned = df.drop(columns=['ingredients', 'prep_time', 'cook_time', 'flavor_profile', 'course', 'state', 'region'])


def updateFile():
    with open(DATAFILE, 'wb') as data:
        pickler = pickle.Pickler(data, -1)
        pickler.dump(USERS)
        data.close()


class Users:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        USERS[self.username] = self  ## adding the User object to dictionary
        updateFile()

class TopScreen(Screen):
    pass
class LoginScreen(Screen):
    def save(self, username, email):
        # print (type(username))
        if (username == "" or email == ""):
            print("enter the details")
        else:
            if (username not in USERS.keys()):
                tmpUsr = Users(username, email)
                print(f"Log: user - {username} added to database!!")
            else:
                print(f"User {username}  logged in")


class FirstScreen(Screen):
    pass


class FPCSScreen(Screen):
    def process(self):
        global word, indices
        word = self.course.text + self.state.text
        print(word)
        indices = give_rec(word)
        print(indices)


class RECScreen(Screen):
    global rec_list
    rec_list = []

    def on_enter(self, *args):
        for i in indices:
            if df_cleaned['diet'].iloc[i] != '-1':
                item = ThreeLineListItem(text=df_cleaned['name'].iloc[i], secondary_text=df_cleaned['diet'].iloc[i]
                                         , tertiary_text=str(df_cleaned['price'].iloc[i]) + '$')

                rec_list.append(item.text)
                self.ids.container1.add_widget(item)

    def save_order(self):
        self.sep_list = self.order_list.text.split(',')
        for i in self.sep_list:
            if i in rec_list:
                print(i, '-order available')

            else:
                print(i, '-order unavailable')


class OptionScreen(Screen):
    pass


class FullMenu1Screen(Screen):
    def on_enter(self, *args):
        for i in range(129):
            if df_cleaned['diet'].iloc[i] != '-1':
                item = ThreeLineListItem(text=df_cleaned['name'].iloc[i], secondary_text=df_cleaned['diet'].iloc[i]
                                         , tertiary_text=str(df_cleaned['price'].iloc[i]) + '$')

                rec_list.append(item.text)
                self.ids.container2.add_widget(item)

    def save_order(self):
        self.sep_list = self.order_list.text.split(',')
        for i in self.sep_list:
            if i in rec_list:
                print(i, '-order available')

            else:
                print(i, '-order unavailable')
class FullMenu2Screen(Screen):
    def on_enter(self, *args):
        for i in range(129,256):
            if df_cleaned['diet'].iloc[i] != '-1':
                item = ThreeLineListItem(text=df_cleaned['name'].iloc[i], secondary_text=df_cleaned['diet'].iloc[i]
                                         , tertiary_text=str(df_cleaned['price'].iloc[i]) + '$')

                rec_list.append(item.text)
                self.ids.container3.add_widget(item)

    def save_order(self):
        self.sep_list = self.order_list.text.split(',')
        for i in self.sep_list:
            if i in rec_list:
                print(i,'-order available')

            else:
                print(i,'-order unavailable')



class LastScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(TopScreen(name='t_s'))
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(FPCSScreen(name='fpcs'))
sm.add_widget(FullMenu1Screen(name='f_p_m'))
sm.add_widget(FullMenu2Screen(name='s_p_m'))
sm.add_widget(RECScreen(name='rec_page'))
sm.add_widget(LastScreen(name='last_screen'))
sm.add_widget(LoginScreen(name='login_screen'))
sm.add_widget(OptionScreen(name='option_screen'))


class KGBApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.theme_style='Dark'
        screen = Builder.load_string(screen_helper)
        return screen


def main():
    # for initally loading all the stuff in the pickle file
    with open(DATAFILE, 'rb') as data:
        try:
            USERS = pickle.load(data)
        except EOFError:
            pass
        data.close()

    # running the app
    app = KGBApp()
    app.run()


# for starting
main()
