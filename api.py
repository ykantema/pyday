import pytest
import requests
import config


class API:
    s = requests.session()
    qn_deployments_url = 'https://yedia-qn-deployment.rnd.cqloud.com/api/2/entities/'

    def login(self):
        res = self.s.get('https://dng1-login.rnd.cqloud.com/api/1.0/login', auth=(config.user, config.pwd))
        assert res.status_code == 200
        print(res)

    def get_qns(self):
        res = self.s.get(self.qn_deployments_url + '?types=qn&entities_list_format=details')
        assert res.status_code == 200
        return res.json()

    def create_qn(self, qn_name):
        json_body = {
            "name": qn_name,
            "type": "qn",
            "asn": "7679",
            "deliveryIf::GigabitEthernet0/0::publicAddress": "172.240.0.10",
            "attributes": {"systemId": qn_name},
            "containedIn": []
        }
        res = self.s.post(self.qn_deployments_url, json=json_body)
        assert res.status_code == 200
        return res.json()

    def get_qn(self, id):
        res = self.s.get(self.qn_deployments_url + '?entities_list_format=details&ids=' + str(id))
        assert res.status_code == 200
        return res.json()['entities'][0]

    def update_qn(self, id, filed, value):
        res = self.get_qn(id)
        res[filed] = value
        res = self.s.put(self.qn_deployments_url + '?id=' +str(id), json=res)
        print(res.json())
        assert res.status_code == 200
        return res.json()

    def delete_qn(self, id):
        res = self.s.delete(self.qn_deployments_url + '?ids=' + str(id))
        assert res.status_code == 200


