# Набор скриптов для редактирования школьного электронного дневника

Набор скриптов позволяет изменять оценки, удалять замечания и добавлять похвалы от учителей.

## Описание скриптов

* `get_schoolkid(name)`

Возвращает учетную запись ученика в дневнике. Аргумент `name` (ФИО ученика) должен быть уникальным, иначе скрипт попроси уточнить запрос.
В случае отсутствия ученика в базе скрипт также сообщит об этом.

* `delete_chastsements(schoolkid)`

Удаляет все замечания ученику, привязанному к учетной записи `schoolkid`.


* `fix_marks(schoolkid)`

Исправляет все двойки и тройки ученика, привязанного к учетной записи `schoolkid`, на пятерки.

* `set_commendation(schoolkid, subject)`

Добавляет случайно выбранную похвалу ученику, привязанному к учетной записи `schoolkid`. Для корректной работы функции необходимо импортировать
модуль random.

##Перед запуском
Для корректно работы в shell не забудьте импортировать необходимые классы и модули командами: 

`from datacenter.models import Chastisement, Schoolkid, Mark, Lesson, Commendation`

`from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned`