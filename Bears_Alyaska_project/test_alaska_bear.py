import requests
from local_host import LOCAL_TCP


class TestBears:
    def test_add_bears(self):
        requests.post(f'http://localhost:{LOCAL_TCP}/bear', json={"bear_type": "BROWN", "bear_name": "mikhail", "bear_age": 10})
        requests.post(f'http://localhost:{LOCAL_TCP}/bear', json={"bear_type": "POLAR", "bear_name": "nino", "bear_age": 15})
        requests.post(f'http://localhost:{LOCAL_TCP}/bear', json={"bear_type": "BLACK", "bear_name": "bruno", "bear_age": 17.5})
        assert len(requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()) == 3, 'Bears not create'

    def test_select_all_bears(self):
        assert requests.get(f'http://localhost:{LOCAL_TCP}/bear'), 'Not data'

    def test_select_one_bear(self):
        self.all_bears = requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()
        self.id_bear = self.all_bears[2]['bear_id']
        assert requests.get(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}').json(), 'Select not bear'

    def test_update_bear_type(self):
        self.all_bears = requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()
        self.id_bear = self.all_bears[1]['bear_id']
        requests.put(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}', json={"bear_type": "BLACK"}),
        select_bear = requests.get(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}').json()
        assert select_bear["bear_type"] == 'BLACK', 'Bear type not change'

    def test_update_bear_name(self):
        self.all_bears = requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()
        self.id_bear = self.all_bears[1]['bear_id']
        requests.put(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}', json={"bear_name": "MIMO"}),
        select_bear = requests.get(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}').json()
        assert select_bear["bear_name"] == 'MIMO', 'Bear name not change'

    def test_update_bear_age(self):
        self.all_bears = requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()
        self.id_bear = self.all_bears[1]['bear_id']
        requests.put(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}', json={"bear_age": 12}),
        self.select_bear = requests.get(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}').json()
        assert self.select_bear["bear_age"] == 12, 'Bear age not change'

    def test_delete_one_bear(self):
        self.all_bears = requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()
        self.id_bear = self.all_bears[0]['bear_id']
        requests.delete(f'http://localhost:{LOCAL_TCP}/bear/{self.id_bear}')
        assert len(requests.get(f'http://localhost:{LOCAL_TCP}/bear').json()) == 2, 'Bear not delete'

    def test_delete_all_bears(self):
        requests.delete(f'http://localhost:{LOCAL_TCP}/bear')
        assert requests.get(f'http://localhost:{LOCAL_TCP}/bear').json() == [], 'Bear not delete'