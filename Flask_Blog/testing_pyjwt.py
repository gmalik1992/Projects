import jwt
from datetime import datetime, timedelta, timezone

# class SampleCode:
#     def generate_confirmation_token(self, expiration=600):
#         reset_token = jwt.encode(
#             {
#                 "confirm": self.id,
#                 "exp": datetime.datetime.now(tz=datetime.timezone.utc)
#                        + datetime.timedelta(seconds=expiration)
#             },
#             current_app.config['SECRET_KEY'],
#             algorithm="HS256"
#         )
#         return reset_token
#
#     def confirm(self, token):
#         try:
#             data = jwt.decode(
#                 token,
#                 current_app.config['SECRET_KEY'],
#                 leeway=datetime.timedelta(seconds=10),
#                 algorithms=["HS256"]
#             )
#         except:
#             return False
#         if data.get('confirm') != self.id:
#             return False
#         self.confirmed = True
#         db.session.add(self)
#         return True

expiration = 30
token = jwt.encode(
            {
                "user_id": 1,
                "exp": datetime.utcnow() + timedelta(seconds=expiration)
            },
            'SECRET_KEY',
            algorithm="HS256"
        )

print(token)

data = jwt.decode(token, 'SECRET_KEY', algorithms=["HS256"])