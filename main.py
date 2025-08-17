from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sqlite3
import os

# Définir les chemins
APP_DIR = os.getcwd()
DB_PATH = os.path.join(APP_DIR, "test_database.db")
IMG_DIR = os.path.join(APP_DIR, "assets")
IMG_DEFAULT = os.path.join(APP_DIR, "assets", "avatar.png")

# Connexion à la base SQLite
if not os.path.exists(DB_PATH):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    open(DB_PATH, 'a').close()

mycon = sqlite3.connect(DB_PATH)
cursor_ = mycon.cursor()

# Définition des écrans
class MainPage(Screen): pass
class Page1(Screen): pass
class Page2(Screen): pass
class Page3(Screen): pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.sss = ""
        self.fff = ""
        self.wdj = ""  # Attribut pour le .kv
        try:
            cursor_.execute("SELECT mat FROM mat")
            r1 = cursor_.fetchone()
            if r1:
                self.wdj = str(r1[0])
        except Exception as e:
            print("Erreur lecture mat:", e)

    def getss(self, xx, yy):
        self.sss = xx.text.strip()
        file_path = os.path.join(IMG_DIR, self.sss + ".png")

        if os.path.exists(file_path):
            yy.source = file_path
        else:
            yy.source = IMG_DEFAULT

        return yy.source

    def o_t_valid(self, widget, sx):
        try:
            cursor_.execute("SELECT Matricule, Username FROM tbl_user WHERE Matricule = ?", (widget.text.strip(),))
            result = cursor_.fetchone()
            if result:
                cursor_.execute("UPDATE mat SET mat=?", (result[0],))
                mycon.commit()
                sx.text = f"You are : {result[1]}"
            else:
                sx.text = "This matricule does not exist"
        except Exception as e:
            sx.text = "Database error"

    def clicked(self, text_, psw):
        try:
            cursor_.execute("SELECT Matricule, Password_, Username FROM tbl_user WHERE Matricule = ?", (text_,))
            result = cursor_.fetchone()
            if result and text_ == str(result[0]) and psw == str(result[1]):
                cursor_.execute("UPDATE mat SET mat=?", (text_,))
                mycon.commit()
                self.root.current = "page1"
            else:
                self.show_dialog("Password check", "Password does not exist !!!")
        except Exception as e:
            self.show_dialog("Password check", "Erreur de connexion à la base")

    def show_dialog(self, title, message):
        self.dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.8, 1),
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        if self.dialog:
            self.dialog.dismiss()

    def close_application(self):
        cursor_.execute("UPDATE mat SET mat=?", ("00000",))
        mycon.commit()
        self.stop()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.icon = os.path.join(APP_DIR, "assets", "R.png")

        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])

        # Charger les fichiers .kv
        Builder.load_file("main_page.kv")
        Builder.load_file("page1.kv")
        Builder.load_file("page2.kv")
        Builder.load_file("page3.kv")

        # Gestion des écrans
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainPage(name="main"))
        screen_manager.add_widget(Page1(name="page1"))
        screen_manager.add_widget(Page2(name="page2"))
        screen_manager.add_widget(Page3(name="page3"))

        return screen_manager

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def switch_screen_left(self, screen_name):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = screen_name

    def switch_screen_right(self, screen_name):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = screen_name

if __name__ == "__main__":
    MainApp().run()
