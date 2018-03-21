

# Cruzaria-platform


### Добро пожаловать!
Это информационная страница проекта [Cruzaria](https://cruzaria.github.com/)


### Cruzaria
Это название платформы, включающее в себя например такую [Витрину курсов](http://54.202.22.177/) для работы со слушателями курсов и подобный [Инструмент создания курсов для преподавателей](http://54.202.22.177:18010)


### Репозиторий
Этот репозиторий содержит boilerplate (начальный прототип) с которого можно начать строительство платформы обучения. Здесь используется Django на backend и React на frontend.

Весь билд включает следующее:

**Frontend**

* [React](https://github.com/facebook/react)
* [React Router](https://github.com/ReactTraining/react-router) Declarative routing for React
* [Babel](http://babeljs.io) for ES6 and ES7 magic
* [Webpack](http://webpack.github.io) for bundling
* [Webpack Dev Middleware](http://webpack.github.io/docs/webpack-dev-middleware.html)
* [Clean Webpack Plugin](https://github.com/johnagan/clean-webpack-plugin)
* [Redux](https://github.com/reactjs/redux) Predictable state container for JavaScript apps 
* [Redux Dev Tools](https://github.com/gaearon/redux-devtools) DevTools for Redux with hot reloading, action replay, and customizable UI. Watch [Dan Abramov's talk](https://www.youtube.com/watch?v=xsSnOQynTHs)
* [Redux Thunk](https://github.com/gaearon/redux-thunk) Thunk middleware for Redux - used in async actions
* [React Router Redux](https://github.com/reactjs/react-router-redux) Ruthlessly simple bindings to keep react-router and redux in sync
* [fetch](https://github.com/github/fetch) A window.fetch JavaScript polyfill
* [tcomb form](https://github.com/gcanti/tcomb-form) Forms library for react
* [style-loader](https://github.com/webpack/style-loader), [sass-loader](https://github.com/jtangelder/sass-loader) and [less-loader](https://github.com/webpack/less-loader) to allow import of stylesheets in plain css, sass and less,
* [font-awesome-webpack](https://github.com/gowravshekar/font-awesome-webpack) to customize FontAwesome
* [bootstrap-loader](https://github.com/shakacode/bootstrap-loader) to customize Bootstrap
* [ESLint](http://eslint.org), [Airbnb Javascript/React Styleguide](https://github.com/airbnb/javascript), [Airbnb CSS / Sass Styleguide](https://github.com/airbnb/css) to maintain a consistent code style and [eslint-plugin-import](https://github.com/benmosher/eslint-plugin-import) to make sure all imports are correct
* [mocha](https://mochajs.org/) to allow writing unit tests for the project
* [Enzyme](http://airbnb.io/enzyme/) JavaScript Testing utilities for React
* [redux-mock-store](https://github.com/arnaudbenard/redux-mock-store) a mock store for your testing your redux async action creators and middleware
* [expect](https://github.com/mjackson/expect) Write better assertions
* [Nock](https://github.com/pgte/nock) HTTP mocking and expectations library
* [istanbul](https://github.com/gotwarlost/istanbul) to generate coverage when running mocha

**Backend**

* [Django](https://www.djangoproject.com/)
* [Django REST framework](http://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Django REST Knox](https://github.com/James1345/django-rest-knox) Token based authentication for API endpoints
* [WhiteNoise](http://whitenoise.evans.io/en/latest/django.html) to serve files efficiently from Django
* [Prospector](http://prospector.landscape.io/en/master/) a complete Python static analysis tool
* [Bandit](https://github.com/openstack/bandit) a security linter from OpenStack Security
* [pytest](http://pytest.org/latest/) a mature full-featured Python testing tool
* [Mock](http://www.voidspace.org.uk/python/mock/) mocking and testing Library
* [Responses](https://github.com/getsentry/responses) a utility for mocking out the Python Requests library





## Инсталляция

Во многих случаях эти пакеты уже установлены и пункт NodeJS можно пропустить

**NodeJS tooling**

* `$ wget -qO- https://deb.nodesource.com/setup_6.x | sudo bash -`
* `$ apt-get install --yes nodejs`
* `$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -`
* `$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list`
* `$ sudo apt-get update && sudo apt-get install yarn`

**Компиляция и запуск node**

Для запуска наберите `yarn run dev` в первой консоли в корне проекта и `python manage.py runserver` во второй коносоле из /src.

* `$ yarn `
* `$ yarn run dev`  # запускаем webpack с watchером отслеживающим изменения в коде

**Компиляция и запуск python**
* `$ virtualenv -p /usr/bin/python3 virtualenv`
* `$ source virtualenv/bin/activate`
* `$ pip install -r py-requirements/dev.txt`

* `$ cd src`
* `$ python manage.py migrate`
* `$ python manage.py loaddata fixtures.json`
* `$ python manage.py runserver`

По-умолчанию сайт будет доступен по адресу: http://localhost:8000/ Если всё нормально, то увидите картинку с React, а на http://localhost:8000/homepage/ приглашение в стиле django-mako. 


## Скриншоты

2 скриншота вам в помощь.

![Screenshot01][1]  

[1]: ./screenshots/screenshot_01.png

![Screenshot02][2]  

[2]: ./screenshots/screenshot_02.png


## Настройки проекта
* `/src/djangoreactredux/settings/dev.py`
* `/src/djangoreactredux/settings/prod.py`



### Версии
Всегда существует множество версий платформ, как результат множества подходов. Так или иначе, но на определенном этапе это всегда случается, когда из проекта с открытым кодом нужно сделать что-нибудь стоящее. Поэтому, Вы вправе сами исправить код, если имеете что сказать.


### Контакты
  [Документация](https://cruzaria.github.com/) и [просто спросить](https://https://github.com/VladimirAndropov)
  
### Взносы (Donate)
Вы можете поблагодарить нас за работу, скажем, ненужным доменом с более-менее подходящим названием для проекта. Или сделать взнос на домен: [gofundme](https://www.gofundme.com/eletsuniversity)
