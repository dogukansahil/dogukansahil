import psutil
import rumps

class DiskSpaceApp(rumps.App):
    def __init__(self):
        super(DiskSpaceApp, self).__init__("Free Space", icon=None)
        self.timer = rumps.Timer(self.update_free_disk_space, 3)
        self.timer.start()
        self.display_as_percentage = False
        self.current_language_code = "en"
        self.translations = {
            "en": "Free Space",
            "zh-Hans": "剩余空间",
            "es": "Espacio Libre",
            "ar": "مساحة حرة",
            "hi": "फ्री स्पेस",
            "fr": "Espace Libre",
            "ru": "Свободное место",
            "bn": "ফ্রি স্পেস",
            "pt": "Espaço Livre",
            "ja": "フリースペース",
            "tr": "Boş Alan",
            "zh-Hant": "剩餘空間",
            "it": "Spazio Libero"
        }

        # Menü öğelerini ekle
        self.menu = [
            rumps.MenuItem("Change Display Mode", callback=self.change_display_mode),
            rumps.MenuItem("Language", callback=None),
            rumps.separator
        ]

        # Dil seçenekleri menüsünü oluştur
        language_menu = self.menu["Language"]
        for lang_code, translation in self.translations.items():
            lang_item = rumps.MenuItem(translation, callback=lambda sender, lang=lang_code: self.change_language(lang))
            language_menu.add(lang_item)

    def update_free_disk_space(self, _):
        free_space = self.get_free_disk_space()
        if self.display_as_percentage:
            self.title = f"{free_space}% {self.translate('Free Space')}"
        else:
            self.title = f"{free_space} GB {self.translate('Free Space')}"

    def get_free_disk_space(self):
        disk_usage = psutil.disk_usage('/')
        if self.display_as_percentage:
            return int(disk_usage.percent)
        else:
            return int(disk_usage.free / (1024 ** 3))

    def change_display_mode(self, _):
        self.display_as_percentage = not self.display_as_percentage
        self.update_free_disk_space(None)

    def change_language(self, language_code):
        self.current_language_code = language_code
        self.update_free_disk_space(None)

    def translate(self, key):
        return self.translations.get(self.current_language_code, key)

if __name__ == "__main__":
    DiskSpaceApp().run()
