from injector import inject
from core.auth.ports import IUserAccessor


class UserService():

    @inject
    def __init__(self, user_accessor: IUserAccessor):
        self.user_accessor = user_accessor

    def get_by_id(self, user_id: int):
        user = self.user_accessor.get_by_id(user_id)
        return user
        