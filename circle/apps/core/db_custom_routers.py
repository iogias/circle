"""
Masuk dalam todo list. Kalo uda punya TIM.

"""


import random


class PrimaryReplicaRouter:
    """
    An example primary/replica router adapted from:
    https://docs.djangoproject.com/en/3.1/topics/db/multi-db/
    """
    route_app_labels = {'auth', 'admin', 'sessions', 'contenttypes'}

    def db_for_read(self, model, **hints):
        """
        Reads go to the random default or replica.
        """
        print(">>>>>>>>>>>>>>>", model._meta.app_label)
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return random.choice(['default', 'replica'])
        # return 'replica'

    def db_for_write(self, model, **hints):
        """
        Writes always go to default.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'default', 'replica'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
