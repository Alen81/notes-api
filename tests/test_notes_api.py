from urllib import response
import pytest
from http import HTTPStatus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import tests.env
import config as app_config
import requests
from api.models import User, Folder, Note, NoteItem, NoteType
from tests.api_client.swagger_client.configuration import Configuration
from tests.api_client.swagger_client.api_client import ApiClient
from tests.api_client.swagger_client.api.auth_api import AuthApi
from tests.api_client.swagger_client.api.folder_api import FolderApi
from tests.api_client.swagger_client.api.note_api import NoteApi
import tests.api_client.swagger_client.models as models


class TestNotesApi:

    data = [
        {
            'name': 'Bill',
            'username': 'Bill10',
            'password': 'pass10',
            'folders': [
                {
                    'name': 'Bill - folder1',
                    'notes': [
                        {
                            'name': 'Bill - folder1 - note1 - list',
                            'type': NoteType.LIST.value,
                            'is_public': False,
                            'items': [
                                {
                                    'text_body': 'a Bill - folder1 - note1 (private) - text body1'  # noqa
                                },
                                {
                                    'text_body': 'z Bill - folder1 - note1 (private)- text body2'  # noqa
                                }
                            ]
                        },
                        {
                            'name': 'Bill - folder1 - note2 - single',
                            'type': NoteType.SINGLE.value,
                            'is_public': True,
                            'items': [
                                {
                                    'text_body': 'm Bill - folder1 - note2 (public) - text body'  # noqa
                                },

                            ]
                        }
                    ]
                },
                {
                    'name': 'Bill - folder2',
                    'notes': [
                        {
                            'name': 'Bill - folder2 - note1 - single',
                            'type': NoteType.SINGLE.value,
                            'is_public': False,
                            'items': [
                                {
                                    'text_body': 'n Bill - folder2 - note1 (private) - text body'  # noqa
                                },

                            ]
                        }
                    ]
                },
                {
                    'name': 'Bill - folder3',
                    'notes': []
                }
            ]
        },
        {
            'name': 'Jack',
            'username': 'Jack20',
            'password': 'pass20',
            'folders': [
                {
                    'name': 'Jack - folder1',
                    'notes': [
                        {
                            'name': 'Jack - folder1 - note1 - single',
                            'type': NoteType.SINGLE.value,
                            'is_public': True,
                            'items': [
                                {
                                    'text_body': 'a Jack - folder1 - note1 (public) - text body'  # noqa
                                },

                            ]
                        }
                    ]
                }
            ]
        },
        {
            'name': 'Lara',
            'username': 'Lara30',
            'password': 'pass30',
            'folders': [
                {
                    'name': 'Lara - folder1',
                    'notes': [
                        {
                            'name': 'Lara - folder1 - note1 - single',
                            'type': NoteType.SINGLE.value,
                            'is_public': True,
                            'items': [
                                {
                                    'text_body': 'c Lara - folder1 - note1 (public) - text body'  # noqa
                                },

                            ]
                        }
                    ]
                }
            ]
        },
    ]

    def setup_class(self):
        pytest.configuration = Configuration()
        self.api_auth = AuthApi(ApiClient(pytest.configuration))
        self.api_folder = FolderApi(ApiClient(pytest.configuration))
        self.api_note = NoteApi(ApiClient(pytest.configuration))

    def user_signup(
        self,
        name: str,
        username: str,
        password: str
    ) -> models.SignupPost:
        signup_post = models.SignupPost(
            name=name,
            username=username,
            password=password,
        )
        return self.api_auth.post_signup_view(signup_post)

    def set_credentials(self, username, password):
        pytest.configuration.api_key_prefix['Authorization'] = 'Basic'
        pytest.configuration.username = username
        pytest.configuration.password = password

    def set_user_credentials(self, user):
        username = user['username']
        password = user['password']
        self.set_credentials(username, password)

    def get_user(self, name):
        return [u for u in self.data if u['name'] == name][0]

    def get_folder_id(self, name):
        return [
            folder['id']
            for users in self.data
            for folder in users['folders'] if folder['name'] == name
        ][0]

    @pytest.mark.mockdata
    def test_signup(self):
        for user in self.data:
            name = user['name']
            username = user['username']
            password = user['password']
            response = self.user_signup(name, username, password)
            assert response.name == name
            assert response.username == username

            # singup user for the second time
            try:
                response = self.user_signup(name, username, password)
            except Exception as e:
                assert e.status == HTTPStatus.BAD_REQUEST

    def test_verify(self):
        for user in self.data:
            self.set_user_credentials(user)
            username = user['username']
            verify_post = models.VerifyPost(username)
            response = self.api_auth.post_verify_view(verify_post)

        username = 'unknown'
        password = 'unknown'
        self.set_credentials(username, password)
        try:
            verify_post = models.VerifyPost(username, password)
            response = self.api_auth.post_verify_view(verify_post)
        except Exception as e:
            assert e.status == HTTPStatus.UNAUTHORIZED

    @pytest.mark.mockdata
    def test_create_folder_note(self):
        for user in self.data:
            self.set_user_credentials(user)

            if 'folders' in user:
                for folder in user['folders']:
                    folder_post = models.FolderPost(name=folder['name'])
                    response = self.api_folder.post_folder_view(folder_post)
                    folder['id'] = response.id
                    folder_id = folder['id']

                    if 'notes' in folder:
                        for note in folder['notes']:
                            items = []
                            if 'items' in note:
                                for item in note['items']:
                                    note_item_post = models.NoteItemPost(**item)  # noqa
                                    items.append(note_item_post)

                            note_post = models.NotePost(
                                folder_id=folder_id,
                                name=note['name'],
                                is_public=note['is_public'],
                                type=note['type'],
                                items=items
                            )
                            response = self.api_note.post_folder_note_view(folder_id, note_post)  # noqa
                            note['id'] = response.id

    def test_get_note(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)
        response = self.api_note.get_note_view()
        assert len(response.items) == 3

    def test_get_note_unauthorized(self):
        response = requests.get(f'{app_config.NOTES_API_SERVER}/note')
        data = response.json()
        assert len(data['items']) == 3
        for note in data['items']:
            assert note['is_public'] is True

    def test_get_note_sort_heading_asc(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)
        response = self.api_note.get_note_view(sort='heading', sortdesc='')
        response_headings = [n.name for n in response.items]
        headings = [
            'Bill - folder1 - note1 - list',
            'Bill - folder1 - note2 - single',
            'Bill - folder2 - note1 - single',
        ]
        assert headings == response_headings

    def test_get_note_sort_heading_desc(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)
        response = self.api_note.get_note_view(sort='heading', sortdesc='true')
        response_headings = [n.name for n in response.items]
        headings = [
            'Bill - folder2 - note1 - single',
            'Bill - folder1 - note2 - single',
            'Bill - folder1 - note1 - list'
        ]
        assert headings == response_headings

    def test_get_note_sort_shared_asc(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)
        response = self.api_note.get_note_view(sort='shared', sortdesc='')
        response_is_publics = [n.is_public for n in response.items]
        is_publics = [False, False, True]
        assert is_publics == response_is_publics

    def test_get_note_sort_shared_desc(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)
        response = self.api_note.get_note_view(sort='shared', sortdesc='true')
        response_is_publics = [n.is_public for n in response.items]
        is_publics = [True, False, False]
        assert is_publics == response_is_publics

    def test_get_note_filter_by_folder(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)

        folder_id = self.get_folder_id('Bill - folder2')
        response = self.api_note.get_note_view(folderid=folder_id)

        response_note_name = response.items[0].name
        note_name = 'Bill - folder2 - note1 - single'
        assert note_name == response_note_name

    def test_get_note_filter_by_public_note_text(self):
        user = self.get_user('Bill')
        self.set_user_credentials(user)

        response = self.api_note.get_note_view(
            notetext='a Jack',
            ispublic='true'
        )

        assert len(response.items) == 1
        response_text_body = response.items[0].items[0].text_body
        text_body = 'a Jack - folder1 - note1 (public) - text body'
        assert text_body == response_text_body

    def test_put_folder(self):
        user = self.get_user('Lara')
        self.set_user_credentials(user)

        folder_id = self.get_folder_id('Lara - folder1')
        new_folder_name = 'Lara - folder1 (changed)'
        folder = models.FolderPost(name=new_folder_name)
        response = self.api_folder.put_folder_id_view(folder_id, folder)

        response = self.api_folder.get_folder_view()
        assert response[0].name == new_folder_name

    def test_put_folder_unauthorized(self):
        user = self.get_user('Lara')
        self.set_user_credentials(user)

        folder_id = self.get_folder_id('Jack - folder1')
        new_folder_name = 'Lara - folder2 (changed)'
        folder = models.FolderPost(name=new_folder_name)
        try:
            response = self.api_folder.put_folder_id_view(folder_id, folder)
        except Exception as e:
            assert e.status == HTTPStatus.FORBIDDEN

    def test_delete_folder(self):
        for user in self.data:
            self.set_user_credentials(user)

            if 'folders' in user:
                for folder in user['folders']:
                    self.api_folder.delete_folder_id_view(folder['id'])

    # def teardown_class(self):
    @pytest.mark.teardown
    def test_delete_user(self):
        engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.query(NoteItem).delete()
        session.query(Note).delete()
        session.query(Folder).delete()
        session.query(User).delete()
        session.commit()


if __name__ == "__main__":
    pytest.main(['-x', __file__, '--verbose', '-s'])
