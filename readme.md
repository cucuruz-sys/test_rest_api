Убедитесь, что у вас установлен Python 3.9 или выше.\
Клонируйте репозиторий:\
git clone https://github.com/cucuruz-sys/test_rest_api.git\ \
перейдите в папку проекта\
Установите зависимости:\
pip install -r requirements.txt\
python -m spacy download en_core_web_sm

Запуск:\
python app.py

Для теста можно запусть requests_examples.py или самостоятельно делать запросы к api.\
Также можно использовать swagger: http://127.0.0.1:8000/docs
