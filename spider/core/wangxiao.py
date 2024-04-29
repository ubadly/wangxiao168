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

    def get_study_plan_list(self, semester: int, page: int = 1, row: int = 200) -> list:
        """
        获取视频学习列表
        :param semester: 学期id
        :param page: 页数
        :param row: 每页的尺寸
        :return:
        """

        params = {
            "page": page,
            "row": row,
            "semester": semester
        }
        url = self.join_url("cjapi/other/student/plan/list")
        response = self._session.get(url, params=params)
        data = response.json()
        return data['data']

    def get_study_plan_time(self, semester: int):
        """
        获取学期开启和结束时间
        :param semester: 学期id
        :return:
        """
        url = self.join_url("cjapi/other/student/semester/studyTime")

        params = {
            "semester": semester
        }
        response = self._session.get(url, params=params)
        data = response.json()

        return data['data']

    def get_study_plan_view(self, view_id: int) -> dict:
        """
        获取学习计划详情
        :param view_id:
        :return:
        """
        url = self.join_url("cjapi/other/student/plan/view")

        params = {
            "id": view_id
        }

        response = self._session.get(url, params=params)

        data = response.json()

        return data['data']
