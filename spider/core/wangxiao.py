# 168网校核心接口部分
from urllib import parse

from requests import Session

from spider.common.enums import School


class WangXiao168:
    def __init__(self, school: School):
        self._school: School = school
        self._session = Session()
        self._init_session()

    def _init_session(self):
        self._session.headers.update({'User-Agent': 'Mozilla/5.0'})
        self._session.proxies = None

    def get_school(self) -> School:
        return self._school

    def get_session(self) -> Session:
        return self._session

    def join_url(self, url: str) -> str:
        """
        拼接连接
        :param url:
        :return:
        """
        return parse.urljoin(self._school.value.url, url)

    def get_semester_list(self) -> list:
        """
        获取学期列表
        :return:
        """
        url = self.join_url("cjapi/other/student/semester/list")
        response = self._session.get(url)
        data = response.json()
        return data['data']
