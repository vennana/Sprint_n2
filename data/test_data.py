BASE_URL = "https://qa-desk.education-services.ru"

# --- Auth ---
DEFAULT_PASSWORD = "Test"
DEFAULT_NAME = "User"

# --- Эндпоинты ---
SIGNUP_ENDPOINT = "/api/signup"
SIGNIN_ENDPOINT = "/api/signin"
CREATE_LISTING_ENDPOINT = "/api/create-listing"
UPDATE_OFFER_ENDPOINT = "/api/update-offer/{ad_id}"
DELETE_LISTING_ENDPOINT = "/api/listings/{ad_id}"

# --- Данные объявления ---
CATEGORIES = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]
CITIES = [
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Екатеринбург",
    "Нижний Новгород",
    "Казань",
]
CONDITIONS = ["Новый", "Б/У"]

DEFAULT_AD = {
    "name": "Тестовое объявление",
    "category": "Авто",
    "condition": "Новый",
    "city": "Москва",
    "description": "Описание тестового объявления",
    "price": "1000",
}

UPDATED_AD = {
    "name": "Обновлённое объявление",
    "category": "Книги",
    "condition": "Б/У",
    "city": "Санкт-Петербург",
    "description": "Новое описание",
    "price": "5000",
}

# --- Ожидаемые сообщения ---
MSG_EMAIL_USED = "Почта уже используется"
MSG_INVALID_CREDENTIALS = "Логин или пароль неверны"
MSG_NO_RIGHTS_TO_EDIT = "Оффер не найден или у вас нет прав на его редактирование"
MSG_AD_DELETED = "Объявление удалено успешно"