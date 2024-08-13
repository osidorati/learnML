from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

# Пример данных
data = {
    'url': [
        "https://thepiratebay.org/torrent/123456",  # пиратская
        "https://example.com/download/free-movie",  # пиратская
        "https://safe-site.com/resource",
        "https://rarbg.to/torrent",  # пиратская
        "https://legal-site.com/resource",
        "https://1337x.to/torrent",  # пиратская
        "https://trustedsource.com/resource",
        "https://28lordserial.site/1361-h2o-prosto-dobav-vody-s29.html"   # пиратская
    ],
    'label': [1, 1, 0, 1, 0, 1, 0, 1]  # 1 - пиратская, 0 - легальная
}

# Создание DataFrame
df = pd.DataFrame(data)

# Преобразование текста URL в числовые признаки
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['url'])

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.2, random_state=42)

# Обучение модели дерева решений
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Оценка модели
accuracy = model.score(X_test, y_test)
print(f"Точность модели: {accuracy * 100:.2f}%")

# Извлечение и вывод правил дерева решений
rules = export_text(model, feature_names=vectorizer.get_feature_names_out())
print(rules)
