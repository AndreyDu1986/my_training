import hashlib

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self._set_password = password
        self.age = age

    def _set_password(self, password: str):
        salt = "salt"
        hashed_password = hashlib.sha256(salt.encode("utf-8") + password.encode("utf-8")).hexdigest()
        self.password = hashed_password

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self._set_password = password

    def is_adult(self):
        return self.age <= 18

class Video:
    def __init__(self, title: str, duration: float, time_now: float, adult_mode: bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def watch(self):
        if self.adult_mode and not self.is_adult():
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        if self.time_now < self.duration:
            print(f"Воспроизведение началось на {self.time_now} секунде.")
            for sec in range(self.time_now, self.duration):
                print(sec)
                if sec % 60 == 0:
                    print(f"Секунды прошли: {sec}")
        else:
            print("Видео уже просмотрено до конца.")

        self.time_now = 0

class UrTube:
    def __init__(self, users: list, videos: list, current_user: str):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def login(self, nickname: str, password: str):
        user = next((user) for user in self.users if user.nickname == nickname and user.password == password)
        if user:
            self.current_user = user
            print(f"Успешный вход в систему.")
        else:
            print("Логин и пароль не совпадают.")

    def logout(self):
        self.current_user = None
        print("Вы вышли из системы.")

    def register(self, nickname: str, password: str, age: int):
        if any(user for user in self.users if user.nickname == nickname):
            print(f"Пользователь с таким ником уже зарегистрирован.")
            return
        user = User(nickname, password, age)
        self.users.append(user)
        self.login(nickname, password)

    def add(self, video: Video):
        if video in self.videos:
            print("Такое видео уже существует.")
            return
        self.videos.append(video)

    def get_videos(self, search_term: str):
        result = [video.title for video in self.videos if search_term.lower() in video.title.lower()]
        return result

    def watch_video(self, title: str):
        video = next((video) for video in self.videos if video.title == title)
        if video:
            video.watch()
        else:
            print("Видео с таким названием не найдено.")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')