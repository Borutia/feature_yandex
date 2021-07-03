from django.test import TestCase

from reports.utils import get_email_link
from . import data_email_test


class EmailGetTestCase(TestCase):
    """Тестирование GET запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )

    def test_email_good(self):
        """Запрос с существующим user_id, проверка статуса 200"""
        response = self.client.get(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['user_id'], data_email_test.GOOD_EMAIL['user_id']
        )
        self.assertEqual(
            response.data['email'], data_email_test.GOOD_EMAIL['email']
        )

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.get(
            '/email/{}'.format(data_email_test.BAD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 404)


class EmailPostTestCase(TestCase):
    """Тестирование POST запроса"""
    def test_email_good(self):
        """Загрузка данных, проверка статуса 201"""
        response = self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)

    def test_email_bad(self):
        """Загрузка невалидного email, проверка статуса 400"""
        response = self.client.post(
            '/email',
            data=data_email_test.BAD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_missing_data(self):
        """Обращение к обработчику с пустым телом, проверка статуса 400"""
        response = self.client.post(
            '/email',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_idempotence(self):
        """
        Обращение к обработчику, проверка идемпотентности,
        проверка статуса 201
        """
        response_1 = self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response_1.status_code, 201)
        response_2 = self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response_1.status_code, 201)
        self.assertEqual(response_1.data, response_2.data)

    def test_wrong_user_id(self):
        """Запрос с отрицательным user_id, проверка статуса 400"""
        response = self.client.post(
            '/email',
            data=data_email_test.BAD_EMAIL_USER_ID,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)


class EmailPatchTestCase(TestCase):
    """Тестирование PATCH запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )

    def test_missing_data(self):
        """Обращение к обработчику с пустым телом, проверка статуса 400"""
        response = self.client.patch(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.patch(
            '/email/{}'.format(data_email_test.BAD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 404)

    def test_idempotence(self):
        """
        Обращение к обработчику, проверка идемпотентности,
        проверка статуса 200
        """
        response_1 = self.client.patch(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response_1.status_code, 200)
        response_2 = self.client.patch(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.data, response_2.data)

    def test_email_bad(self):
        """Загрузка невалидного email, проверка статуса 400"""
        response = self.client.patch(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            data=data_email_test.BAD_EMAIL,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)


class EmailDeleteTestCase(TestCase):
    """Тестирование DELETE запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )

    def test_delete(self):
        """Проверка на удаление, статус 204"""
        response = self.client.delete(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 204)

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.delete(
            '/email/{}'.format(data_email_test.BAD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 404)

    def test_idempotence(self):
        """
        Обращение к обработчику, проверка идемпотентности,
        проверка статуса 204
        """
        response_1 = self.client.delete(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response_1.status_code, 204)
        response_2 = self.client.delete(
            '/email/{}'.format(data_email_test.GOOD_USER_ID),
            content_type='application/json',
        )
        self.assertEqual(response_2.status_code, 204)


class EmailConfirmTestCase(TestCase):
    """Тестирование confirm POST запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=data_email_test.GOOD_EMAIL,
            content_type='application/json',
        )

    def test_confirm(self):
        """Проверка подтверждения email, статус 200"""
        response = self.client.get(
            get_email_link(
                email=data_email_test.GOOD_EMAIL['email'],
                user_id=data_email_test.GOOD_EMAIL['user_id'],
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.get(
            get_email_link(
                email=data_email_test.GOOD_EMAIL['email'],
                user_id=data_email_test.BAD_USER_ID,
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_wrong_email(self):
        """Запрос с неверным email, проверка статуса 404"""
        response = self.client.get(
            get_email_link(
                email='bad_test@yandex.ru',
                user_id=data_email_test.GOOD_EMAIL['user_id'],
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_idempotence(self):
        """
        Обращение к обработчику, проверка идемпотентности,
        проверка статуса 200
        """
        response_1 = self.client.get(
            get_email_link(
                email=data_email_test.GOOD_EMAIL['email'],
                user_id=data_email_test.GOOD_EMAIL['user_id'],
            )
        )
        self.assertEqual(response_1.status_code, 200)
        response_2 = self.client.get(
            get_email_link(
                email=data_email_test.GOOD_EMAIL['email'],
                user_id=data_email_test.GOOD_EMAIL['user_id'],
            )
        )
        self.assertEqual(response_2.status_code, 200)
