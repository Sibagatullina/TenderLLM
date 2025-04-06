# TenderLLM

# RAG Chatbot для портала госзакупок

## 📌 О проекте

Чат-бот с архитектурой RAG (Retrieval-Augmented Generation) для автоматизации ответов на вопросы о государственных закупках. Решение предназначено для поставщиков и закупщиков, работающих с порталами госзакупок.

## 🌟 Ключевые особенности

- Гибридный поиск: Комбинация семантического и ключевого поиска
- Контекстные ответы: Генерация ответов на основе актуальных документов
- Прозрачность: Отображение источников информации
- Адаптивность: Поддержка различных баз знаний и коллекций документов

## 🛠 Технологический стек

### Основные компоненты
- Язык программирования: Python 3.10+
- Векторная БД: Milvus (для хранения и поиска чанков)
- Языковая модель: YandexGPT-5-Lite-8B-instruct
- Фронтенд: Streamlit (веб-интерфейс)
- Алгоритм поиска: BM25 (Best Matching 25)

### Вспомогательные технологии
- PyMilvus: Python SDK для работы с Milvus
- OpenAI-совместимый API: Для взаимодействия с Yandex LLM
- Streamlit-chat: Для отображения истории сообщений

## ⚙️ Установка и настройка

### Предварительные требования
- Python 3.10 или новее
- Docker (для локального запуска Milvus)
- Учетные записи:
  - Доступ к API Yandex GPT
  - (Опционально) Облачный инстанс Milvus

### Установка

1. Клонируйте репозиторий:
```bash
git clone [https://github.com/yourusername/supplier-portal-chatbot.git](https://github.com/Sibagatullina/TenderLLM.git)
cd llm_bot
```


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   
│ 
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         llm_bot and configuration for tools like black
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── llm_bot   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes llm_bot a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    │
    ├── app.py             <- main file
    │
    └── search.py             <- search functions
```

--------

