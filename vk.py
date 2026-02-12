from tkinter import *
import os

# ========== ПОЛУЧАЕМ ПАПКУ СКРИПТА ==========
script_dir = os.path.dirname(os.path.abspath(__file__))

def get_image_path(filename):
    """Возвращает полный путь к изображению в папке скрипта"""
    return os.path.join(script_dir, filename)

# ========== ИНИЦИАЛИЗАЦИЯ ОКНА ==========
root = Tk()
root.geometry('900x700')
root.configure(bg='#f0f0f0')

# ========== СКРУГЛЕНИЕ ОКНА ==========
def rounded_rect(canvas, x1, y1, x2, y2, radius=15, **kwargs):
    points = [
        x1 + radius, y1, x2 - radius, y1, x2, y1,
        x2, y1 + radius, x2, y2 - radius, x2, y2,
        x2 - radius, y2, x1 + radius, y2, x1, y2,
        x1, y2 - radius, x1, y1 + radius, x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def open_profile(event=None):
    print("Переход в профиль")

def on_link_click(name):
    print(f"Клик по: {name}")

def on_enter(label):
    label.config(fg='#ff61f5')

def on_leave(label):
    label.config(fg='#575757')  

# ========== ПРОВЕРКА НАЛИЧИЯ ФАЙЛОВ ==========
required_files = ["logo.png", "ava.png", "photo_1.png", "photo_2.png"]
missing = [f for f in required_files if not os.path.exists(get_image_path(f))]

if missing:
    from tkinter import messagebox
    messagebox.showerror("Ошибка", 
        f"Отсутствуют файлы в папке:\n{script_dir}\n\nНе найдены:\n" + "\n".join(missing) + 
        "\n\nПоложите все 4 PNG-файла в эту папку и перезапустите программу.")
    root.destroy()
    exit()

# ========== ШАПКА ==========
header_container = Frame(root, bg='#34c759', padx=2, pady=2)
header_container.pack(fill='x', side='top')

header = Frame(header_container, bg='#ebffef', height=60)
header.pack(fill='x')
header.pack_propagate(False)

# Логотип
logo_img = PhotoImage(file=get_image_path("logo.png")).subsample(14, 14)
Label(header, image=logo_img, bg='#ebffef').pack(side='left', padx=(10, 5))
root.logo_img = logo_img

Label(header, text='вконтакте', font=('Arial', 20, 'bold'), fg='black', bg='#ebffef').pack(side='left')

# Поисковая строка
search_frame = Frame(header, bg='#ebffef')
search_frame.pack(side='left', padx=20, fill='x', expand=True)

search = Entry(search_frame, font=('Arial', 12), bd=0, relief='flat', 
               bg='#e9e9e9', fg='#525252')
search.pack(fill='x', padx=10, pady=10, ipady=4)
search.insert(0, '🔍 поиск')

def on_focus_in(event):
    if search.get() == '🔍 поиск':
        search.delete(0, END)
        search.config(fg='#525252')

def on_focus_out(event):
    if not search.get():
        search.insert(0, '🔍 поиск')
        search.config(fg='#888888')

search.bind('<FocusIn>', on_focus_in)
search.bind('<FocusOut>', on_focus_out)

# Правая часть шапки
right_frame = Frame(header, bg='#ebffef')
right_frame.pack(side='right', padx=10)

# Кнопка профиля с аватаркой
profile_frame = Frame(right_frame, bg='#ebffef', cursor='hand2')
profile_frame.pack(side='left', padx=(0, 10))
profile_frame.bind('<Button-1>', open_profile)

profile_btn = Label(profile_frame, text='ПРОФИЛЬ', font=('Arial', 11), 
                    bg='#ebffef', fg='#000000', cursor='hand2')
profile_btn.pack(side='left')
profile_btn.bind('<Button-1>', open_profile)

# Аватарка
ava_img = PhotoImage(file=get_image_path("ava.png")).subsample(24, 24)
ava_label = Label(profile_frame, image=ava_img, bg='#ebffef', cursor='hand2')
ava_label.pack(side='left', padx=(5, 0))
ava_label.bind('<Button-1>', open_profile)
root.ava_img = ava_img

# Колокольчик
bell_btn = Button(right_frame, text='🔔', font=('Arial', 18), bg='#ebffef', 
                  fg='black', bd=0, relief='flat', cursor='hand2', 
                  activebackground='#d0f0d0')
bell_btn.pack(side='left')

# ========== ОСНОВНОЙ КОНТЕЙНЕР ==========
main_container = Frame(root, bg='#f0f0f0')
main_container.pack(fill='both', expand=True)

# ========== ЛЕВАЯ ПАНЕЛЬ НАВИГАЦИИ ==========
nav_frame = Frame(main_container, bg='#eeeeee', width=200)
nav_frame.pack(side='left', fill='y', pady=(10, 20))
nav_frame.pack_propagate(False)

# Кнопки навигации
nav_items = [('👤', 'ПРОФИЛЬ'), ('📰', 'ЛЕНТА'), ('👥', 'ДРУЗЬЯ'), ('💬', 'МЕССЕНДЖЕР')]
for symbol, text in nav_items:
    btn = Button(nav_frame, text=f'{symbol} {text}', font=('Arial', 11), 
                 bg='#eeeeee', fg='#000000', bd=0, anchor='w', padx=20, pady=8,
                 activebackground='#eeeeee', activeforeground='#ff61f5',
                 relief='flat', cursor='hand2')
    btn.pack(fill='x', pady=2)

# ========== ССЫЛКИ (поменяны местами) ==========
# Сначала "Блог, Разработчикам..."
footer_text = Label(nav_frame, text='Блог • Разработчикам • Для бизнеса • Авторам • Действия • Ещё', 
                    font=('Arial', 7, 'underline'), bg='#eeeeee', fg='#575757', 
                    justify='left', cursor='hand2', wraplength=180)
footer_text.pack(anchor='w', padx=10, pady=(40, 5))
footer_text.bind('<Button-1>', lambda e: on_link_click('Все ссылки'))
footer_text.bind('<Enter>', lambda e: on_enter(footer_text))
footer_text.bind('<Leave>', lambda e: on_leave(footer_text))

# Потом "Применяются рекомендательные технологии"
footer_text2 = Label(nav_frame, text='Применяются рекомендательные технологии', 
                     font=('Arial', 7, 'underline'), bg='#eeeeee', fg='#575757', 
                     justify='left', cursor='hand2', wraplength=160)
footer_text2.pack(anchor='w', padx=10, pady=(5, 20))
footer_text2.bind('<Button-1>', lambda e: on_link_click('Рекомендательные технологии'))
footer_text2.bind('<Enter>', lambda e: on_enter(footer_text2))
footer_text2.bind('<Leave>', lambda e: on_leave(footer_text2))

# ========== ЦЕНТРАЛЬНЫЙ КОНТЕНТ ==========
content = Frame(main_container, bg='#eeeeee')
content.pack(side='left', fill='both', expand=True, padx=20, pady=20)

feed_container = Frame(content, bg='#eeeeee')
feed_container.pack(fill='both', expand=True)

header_feed_canvas = Canvas(feed_container, bg='#eeeeee', highlightthickness=0, height=40)
header_feed_canvas.pack(fill='x', pady=(0, 10))

def draw_header_feed():
    header_feed_canvas.delete('all')
    width = header_feed_canvas.winfo_width()
    if width > 10:
        rounded_rect(header_feed_canvas, 0, 0, width, 40, radius=15, 
                     fill='#3363ff', outline='')
        header_feed_canvas.create_text(width//2, 20, text='ЛЕНТА НОВОСТЕЙ', 
                                       font=('Arial', 15, 'bold'), fill='#ffffff')

header_feed_canvas.bind('<Configure>', lambda e: draw_header_feed())
root.after(100, draw_header_feed)

posts_container = Frame(feed_container, bg='white')
posts_container.pack(fill='both', expand=True)

# ========== РЕКЛАМА ==========
ad_frame = Frame(main_container, bg='#f0f0f0', width=200)
ad_frame.pack(side='right', fill='y', pady=(50, 20))
ad_frame.pack_propagate(False)

ad_img1 = PhotoImage(file=get_image_path("photo_1.png")).subsample(2, 2)
ad_label1 = Label(ad_frame, image=ad_img1, bg='#f0f0f0', relief='flat')
ad_label1.pack(pady=(0, 15))
root.ad_img1 = ad_img1

ad_img2 = PhotoImage(file=get_image_path("photo_2.png")).subsample(2, 2)
ad_label2 = Label(ad_frame, image=ad_img2, bg='#f0f0f0', relief='flat')
ad_label2.pack(pady=(0, 20))
root.ad_img2 = ad_img2

# ========== ЗАПУСК ПРИЛОЖЕНИЯ ==========
root.mainloop()

