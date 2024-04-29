# 168网校核心接口部分
from urllib import parse

from requests import Session

from spider.common.enums import School
from spider.common.utils import svg2png


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

    def do_login(self, username: str, password: str):
        """
        登陆
        :param username:
        :param password:
        :return:
        """
        url = self.join_url("cjapi/other/student/login")

        key, code = self.get_capt_code()
        data = {
            "username": username,
            "password": password,
            "code": str(code),
            "codekey": key,
            "school_id": 28
        }

        response = self._session.post(url, json=data)

        data = response.json()

        if data['errCode'] == 200 and data['message'] == '登陆成功' and data['data'] and data['data'].get("token"):
            token = data['data']['token']
            self._session.headers.update({'Authorization': token})
        return data

    def set_token(self, token: str):
        """
        设置登陆信息

        :param token:
        :return:
        """
        self._session.headers.update({'Authorization': token})

    def join_url(self, url: str) -> str:
        """
        拼接连接
        :param url:
        :return:
        """
        return parse.urljoin(self._school.value.url, url)

    def get_capt_code(self):
        url = "https://xatu.168wangxiao.com/cjapi/other/code"
        response = self._session.get(url)
        data = response.json()
        code = svg2png(data['data']['img'])
        key = data['data']['codekey']

        return key, code

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
            "rows": row,
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

    def get_study_chapter_view(self, view_id: int, tpc_id: int):
        """
        获取视频详情信息

        :param view_id:
        :param tpc_id:
        :return:
        """

        url = self.join_url("cjapi/other/student/chapter/view")

        params = {
            "id": view_id,
            "tpcid": tpc_id
        }

        response = self._session.get(url, params=params)

        data = response.json()

        return data['data']

    def update_video_status(self, tpc_id: int, curriculum_id: int, chapter_id: int, video_id: int, status_type: int, process: int):
        """
        更新视频状态
        :param tpc_id:
        :param curriculum_id:
        :param chapter_id:
        :param video_id: 食品id
        :param status_type: 状态类型
        :param process: 进度
        :return:
        """
        url = self.join_url("cjapi/other/student/curriculum/progress/update/v2")

        data = {
            "tpcId": tpc_id,
            "curriculumid": curriculum_id,
            "chapterid": chapter_id,
            "videoid": video_id,
            "type": status_type,
            "progress": process
        }

        response = self._session.put(url, json=data)

        data = response.json()

        return data['data']
