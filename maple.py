from typing import Any, Union
import requests


class Maple:
    """
    A package for making API Wrappers for Django Ninja or Fast API 🍁
    """

    BASE_URL: str = ""

    AUTHORIZATION_KEY: str = ""
    PARAM_NAME: str = "X-API-KEY"
    HEADERS: dict = {}
    CLIENT = requests

    def __init__(
        self,
        base_url: str,
        authorization_key: str = AUTHORIZATION_KEY,
        param_name: str = PARAM_NAME,
        headers: dict = HEADERS,
    ):
        self.BASE_URL = base_url
        self.AUTHORIZATION_KEY = authorization_key
        self.PARAM_NAME = param_name
        self.HEADERS = headers

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return f"{self.__class__.__name__}: {self.BASE_URL}"

    def _make_request(
        self,
        endpoint: str,
        method: str,
        params: Union[dict, None] = None,
        data: Union[dict, None] = None,
    ) -> requests.Response:
        """
        Makes a request to the API.
        """
        headers = {
            **{self.PARAM_NAME: self.AUTHORIZATION_KEY, "Referer": self.BASE_URL},
            **self.HEADERS,
        }
        url: str = f"{self.BASE_URL}{endpoint}"
        return self.CLIENT.request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
        )

    def get(self, endpoint: str, params: Union[dict, None] = None):
        """
        Makes a `GET` request to the API.
        """
        return self._make_request(endpoint, "GET", params=params)

    def post(self, endpoint: str, data: Union[dict, None] = None):
        """
        Makes a `POST` request to the API.
        """
        return self._make_request(endpoint, "POST", data=data)

    def put(self, endpoint: str, data: Union[dict, None] = None):
        """
        Makes a `PUT` request to the API.
        """
        return self._make_request(endpoint, "PUT", data=data)

    def patch(self, endpoint: str, data: Union[dict, None] = None):
        """
        Makes a `PATCH` request to the API.
        """
        return self._make_request(endpoint, "PATCH", data=data)

    def delete(self, endpoint: str):
        """
        Makes a `DELETE` request to the API.
        """
        return self._make_request(endpoint, "DELETE")

    def set_attr(self, attr: str, value: Any):
        """
        Sets an attribute on the object.
        """
        setattr(self, attr, value)
